#include <stdio.h>
#include <stdlib.h>
int main()
{
   FILE* fp1;
   int number;
   char c;

   fp1 = fopen("numbers.txt", "w");

   if (!fp1)
   {
       printf("File does not opened");
       exit(1);
   }
   
    int i =1;
   while (i<5)
   {   
    //    c = fgetc(fp1);
    //    if(number == EOF)
    //         break;
    //    else
    //    {
       scanf("%d", &number);
       fputs(number,fp1);
    //    }
    i++;
   }

   fclose(fp1);
}