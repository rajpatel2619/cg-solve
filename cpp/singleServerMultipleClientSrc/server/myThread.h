#if !defined myThread_H
#define myThread_H

#define _WIN32_WINNT 0x0400
#include <windows.h>
#include <string>
using namespace std;

class myThread  
{

public:

    myThread(
		LPTHREAD_START_ROUTINE pThreadFunc,    // address of thread callback
		LPVOID pThreadFuncParameter=NULL,      // address of callback's parameter,
		DWORD  exeFlags=0,                     // creation flag
		DWORD  sSize=0,                        // stack size
		BOOL   inheritable=FALSE               // inheritable
	);        

    ~myThread();

public:

	void execute();
	void waitForThreadToFinish();    
	void suspend();
    void resume();

	void setThreadPriority(int);
    int  getThreadPriority();

    void disablePriorityBoost(BOOL);
	BOOL isPriorityBoostDisabled();

    void setProcessorMask(DWORD);
	void setIdealProcessor(DWORD);

	LPVOID getThreadArgument() { return threadArgument; }
    DWORD getExitCode();    
	DWORD getThreadId();
	void  getThreadStatistics(LPFILETIME,LPFILETIME,LPFILETIME,LPFILETIME);

private:
	
    HANDLE thread;
    DWORD  threadId;
	DWORD  stackSize;
	DWORD  executeFlag;
	LPTHREAD_START_ROUTINE threadFunction;
	LPVOID threadArgument;
    LPSECURITY_ATTRIBUTES sa;
    DWORD exitCode;

private:

    static void getErrorDetail(int&,string&);
};
#endif