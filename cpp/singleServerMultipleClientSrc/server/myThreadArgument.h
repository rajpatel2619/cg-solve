#if !defined myThreadArgument_H
#define myThreadArgument_H

class mySemaphore;
class myTcpSocket;
class myEvent;

const int MAX_NUM_CLIENTS = 10;

class myThreadArgument
{

private:

	// you have to change here to fit your needs

	mySemaphore* coutSemaphore;       // semaphore for accessing the log file
	myTcpSocket* clientConnection;    // the connecting socket to the client
	string hostName;                // the name of the client
	myThreadArgument* clientArgument[MAX_NUM_CLIENTS];
    int numOfConnectedClients;

	// but the exitEvent is always needed
	myEvent* exitEvent;
	bool signalToEnd;

public:

	// you have to change here to fit your needs
	myThreadArgument(myTcpSocket* client,mySemaphore* coutSem,string& cName);
	~myThreadArgument() ;

	// use the accessor functions that fit your needs

	mySemaphore* getCoutSemaphore()     { return coutSemaphore; }
	myTcpSocket* getClientConnect()     { return clientConnection; }
	string&      getHostName()          { return hostName; }
	bool getSignalToEnd()               { return signalToEnd; }
	void setSignalToEnd(bool s)         { signalToEnd = s; }

	void addClientArgument(myThreadArgument*);
	myThreadArgument* getClientArgument(int);

	// do not change here
    myEvent* getExitEvent() { return exitEvent;}
};

#endif