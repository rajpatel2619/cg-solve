#include <iostream>
using namespace std;

int result(int n){
    if(n<=10){
        return n;
    }else{
        int a = n%10;
        int b = n/10;
        return a+result(a+b);
    }
}
int main(){
    cout<<result(5126);
    return 0;
}