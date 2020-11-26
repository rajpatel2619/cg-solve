
#include <iostream>
#include <fstream>
using namespace std;

int step = 0;

// .................................................................

//  function to swap two elements  
void swap(int* a, int* b)  
{  
    step++;
    int t = *a;     
    *a = *b;  
    *b = t;  
}  
  
int partition (int arr[], int low, int high)  
{  
    int pivot = arr[high]; // pivot  
    int i = (low - 1); // Index of smaller element  
  
    for (int j = low; j <= high - 1; j++)  
    {  
        // If current element is smaller than the pivot  
        if (arr[j] < pivot)  
        {  
            i++; // increment index of smaller element  
            swap(&arr[i], &arr[j]);  
        }  
    }  
    swap(&arr[i + 1], &arr[high]);  
   
    return (i + 1);  
}  
// .................................................................

// displaying array
void display(int a[],int size){
    for(int i=0;i<size;i++){
        cout<<a[i]<<endl;
    }
}

// find count value by - sorting of array using divide and conquer ....
void countBySort(int a[],int low,int high){
    if (low < high)  
    {  
        int pi = partition(a, low, high);  
        countBySort(a, low, pi - 1);  
        countBySort(a, pi + 1, high);  
    }  
    

}



int main() {

    int x,size;
    int array[size];
    ifstream inputFile;
    
    inputFile.open("input.txt");
    if (!inputFile) {
        cout << "Unable to open file";
        exit(1);
    }


    int i = 1;
    while (inputFile >> x) {
        if(i==1){
            size = x;
        }else{
            array[i-2]=x;
        }
        i++;  
    }

    int a=0; // refreshing..
    countBySort(array,0,size-1);
    display(array,size);

    cout<<step<<endl;

   
    return 0;
}
