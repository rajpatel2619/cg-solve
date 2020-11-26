#include "..\myEvent\myEvent.h"
#include "myThreadArgument.h"

myThreadArgument::myThreadArgument(myTcpSocket* client,mySemaphore* coutSem,string& cName)
{
	coutSemaphore = coutSem;
	clientConnection = client;
	hostName = cName;
	exitEvent = new myEvent();
	signalToEnd = false;

	for ( int i = 0; i < MAX_NUM_CLIENTS; i ++ ) clientArgument[i] = NULL;
    numOfConnectedClients = 0;
}

myThreadArgument::~myThreadArgument() 
{
	delete exitEvent;
}

void myThreadArgument::addClientArgument(myThreadArgument* argument)
{
	if ( argument )
		clientArgument[numOfConnectedClients++] = argument;
}

myThreadArgument* myThreadArgument::getClientArgument(int index)
{
	if ( index < MAX_NUM_CLIENTS ) return clientArgument[index];
	return NULL;
}


