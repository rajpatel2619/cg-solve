
// ................. program is written in " C " - Language ................
#include <stdio.h>
#include <stdlib.h> 
#include<time.h> 

// total amount which is shared in each loop 
long int total=0;

//deposite  
int deposite(){
    for(int i=0;i<90;i++){
        int x=rand();
        total+=x;
        printf("%d$ deposited, total available balance is: %ld$ \n",x,total); 
        // in every print statement ' $ ' is just use for money representation.
    }
}

//withdraw 
int withdraw(){
    for(int i=0;i<90;i++){
        int x=rand();
        if(x>total){
            printf("Insufficiant Balance, withdrawl request %ld$ available balance %d$ \n",x,total);
        }else{
            total-=x;
            printf("%d$ withdraw, total available balance is: %ld$ \n",x,total); 
        }
    }
}

int main()
{

// current time as seed for random generator
srand(time(0)); 

//calling depostite 
deposite();

// calling withdraw
withdraw();

return 0;

}