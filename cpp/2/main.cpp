#include <iostream>
#include <string>
#include <stack>

using namespace std;
int main(){
    stack<char> s;
    bool eCheck = false;
    string str = "(x-y)+5))";

    for (int j = 0; j < str.length(); j++)
    {
        if(str[j]=='(')
            s.push(str[j]);
        else if((str[j]==')') && !s.empty())
            s.pop();
        else if((str[j]==')') && s.empty())
            eCheck=true;
    }

    if(!s.empty()){
        eCheck=true;
    }

    if(eCheck)
        cout<< "Errors occurred\n";
    else
        cout<<"No errors occurred\n";
    
    return EXIT_SUCCESS;   
}