#include "..\myEvent\myEvent.h"
#include "mySocket.h"
#include "..\myLog\myLog.h"
#include "..\myException\myException.h"
#include "..\myHostInfo\myHostInfo.h"
#include "..\mySemaphore\mySemaphore.h"
#include "..\myThread\myThread.h"
#include "myThreadArgument.h"

myLog winLog;

DWORD WINAPI clientHandleThread(LPVOID threadInfo)
{
	// this structure will contain all the data this callback will work on
    myThreadArgument* clientArgument = (myThreadArgument*)threadInfo;
		
	// the semamphore to protect the access to the std output
    mySemaphore* coutSemaphore = clientArgument->getCoutSemaphore();

	// get the client connection: receiving messages from client and
	// sending messages to the client will all be done by using
	// this client connection
	myTcpSocket* clientConnection = clientArgument->getClientConnect();
	string clientName = clientArgument->getHostName();

	// the server is communicating with this client here
	while(1)
	{
		string messageFromClient = "";
		
		// receive from the client

        int numBytes = clientConnection->recieveMessage(messageFromClient);
		if ( numBytes == -99 ) break;

		// write to the console and the log file, so lock the semaphore
		coutSemaphore->lock();

		cout   << "[RECV fr " << clientName << "]: " << messageFromClient << endl;
		winLog << "[RECV fr " << clientName << "]: " << messageFromClient << endl;

		// if the client wants to discount
		if ( messageFromClient.compare("quit") == 0 || messageFromClient.compare("Quit") == 0 )
		{
			coutSemaphore->unlock();
			break;
		}
		else // send to the client
		{
			char messageToClient[MAX_MSG_LEN+1];
			memset(messageToClient,0,sizeof(messageToClient));
			cout << "[SEND to " << clientName << "]: ";
			cin.getline(messageToClient,MAX_MSG_LEN);
			winLog << "[SEND to " << clientName << "]: " << messageToClient << endl;
			clientConnection->sendMessage(string(messageToClient));
			coutSemaphore->unlock();
		}
    }

	// if we reach here, this session with the client is done,
	// so we set the event on this thread to inform the main
	// control that this session is finished
	clientArgument->getExitEvent()->setEvent();
	return 1;
}

DWORD WINAPI serverHandleThread(LPVOID threadInfo)
{
	// this structure will contain all the data this callback will work on
    myThreadArgument* serverArgument = (myThreadArgument*)threadInfo;
		
	// the semamphore to protect the access to the std output
    mySemaphore* coutSemaphore = serverArgument->getCoutSemaphore();

	// get the server
	myTcpSocket* myServer = serverArgument->getClientConnect();
	string serverName = serverArgument->getHostName();

	// bind the server to the socket
    myServer->bindSocket();
	cout   << endl << "server finishes binding process... " << endl;
	winLog << endl << "server finishes binding process... " << endl;
	
	// server starts to wait for client calls
	myServer->listenToClient();
	cout   << "server is waiting for client calls ... " << endl;
	winLog << "server is waiting for client calls ... " << endl;
	
	// server starts to listen, and generates a thread to 
	// handle each client

	myThreadArgument* clientArgument[MAX_NUM_CLIENTS];
	myThread* clientHandle[MAX_NUM_CLIENTS];
	for ( int i = 0; i < MAX_NUM_CLIENTS; i++ )
	{
		clientArgument[i] = NULL;
		clientHandle[i] = NULL;
	}
	int currNumOfClients = 0;

	while ( 1 )
	{
		// wait to accept a client connection.  
		// processing is suspended until the client connects
    	myTcpSocket* client;    // connection dedicated for client communication
		string clientName;      // client name 
		client = myServer->acceptClient(clientName);	
		clientName = clientName + "-" + char(65+currNumOfClients);

		// lock the std out so we can write to the console
		coutSemaphore->lock();
        cout   << endl << "==> A client from [" << clientName << "] is connected!" << endl << endl;
		winLog << endl << "==> A client from [" << clientName << "] is connected!" << endl << endl;
		coutSemaphore->unlock();

		// for this client, generate a thread to handle it
		if ( currNumOfClients < MAX_NUM_CLIENTS-1 )
		{
			clientArgument[currNumOfClients] = new myThreadArgument(client,coutSemaphore,clientName);
			clientHandle[currNumOfClients] = new myThread(clientHandleThread,(void*)clientArgument[currNumOfClients]);
			serverArgument->addClientArgument(clientArgument[currNumOfClients]);
			clientHandle[currNumOfClients]->execute();
			currNumOfClients++;
		}
	}

    return 1;
}

int main()
{
	// build a semaphore so we can synchronize the access to std cout
	// also includes the log file
	mySemaphore coutSemaphore(string(""),1);

	// Initialize the winsock library
	myTcpSocket::initialize();

	// create the server: local host will be used as the server, let us 
	// first use myHostInfo class to show the name and IP address 
	// of the local host
	winLog << endl;
	winLog << "Retrieve the local host name and address:" << endl;
	
    myHostInfo serverInfo;
	string serverName = serverInfo.getHostName();
    string serverIPAddress = serverInfo.getHostIPAddress();
	cout << "my localhost (server) information:" << endl;
	cout << "	Name:    " << serverName << endl;
    cout << "	Address: " << serverIPAddress << endl;
	winLog << "		==> Name: " << serverName << endl;
	winLog << "		==> Address: " << serverIPAddress << endl;

	// open socket on the local host(server) and show its configuration
	myTcpSocket myServer(PORTNUM);
	cout   << myServer;
	winLog << myServer;

	// create a thread to implement server process: listening to the socket,
	// accepting client calls and communicating with clients. This will free the 
	// main control (see below) to do other process.
	myThreadArgument* serverArgument = new myThreadArgument(&myServer,&coutSemaphore,serverName);
	myThread* serverThread = new myThread(serverHandleThread,(void*)serverArgument);
	serverThread->execute();

	// main control: since the serverThread is handling the server functions,
	// this main control is free to do other things.
	while ( 1 )
	{
		// do whatever you need to do here, I am using Sleep(x) 
		// to make a little delay, pretending to be the other 
		// possible processings.
		Sleep(50000);

		// report the server status
		coutSemaphore.lock();
		cout   << endl << "-----------------------------------------------------------------" << endl;
		winLog << endl << "-----------------------------------------------------------------" << endl;
		cout   << "server (name:" << serverName << ") status report:" << endl;
		winLog << "server (name:" << serverName << ") status report:" << endl;
		cout   << "   the following clients have successfully connected with server: " << endl;
		winLog << "   the following clients have successfully connected with server: " << endl;
		for ( int i = 0; i < MAX_NUM_CLIENTS; i ++ )
		{
			myThreadArgument* clientInfo = serverArgument->getClientArgument(i);
			if ( clientInfo ) 
			{
				cout   << "         " << clientInfo->getHostName() << endl;
				winLog << "         " << clientInfo->getHostName() << endl;
			}
		}
		cout   << "   the following clients have shutdown the connection: " << endl;
		winLog << "   the following clients have shutdown the connection: " << endl;
		for ( i = 0; i < MAX_NUM_CLIENTS; i ++ )
		{
			myThreadArgument* clientInfo = serverArgument->getClientArgument(i);
			if ( clientInfo && clientInfo->getExitEvent()->waitForEvent(0) )
			{
				clientInfo->setSignalToEnd(true);
				cout   << "         " << clientInfo->getHostName() << endl;
				winLog << "         " << clientInfo->getHostName() << endl;
			}
		}
        cout   << "-----------------------------------------------------------------" << endl << endl;
		winLog << "-----------------------------------------------------------------" << endl << endl;
		coutSemaphore.unlock();
	}

    return 1;
}

