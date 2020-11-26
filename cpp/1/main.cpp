// ...... I am using c++ for wirting this code ....

#include <iostream>
#include <cmath>

using namespace std;

class Tringle{
    private:
        int x1,y1,x2,y2,x3,y3;
    public:
    int isValidate=0;
    // default constructer.........
        Tringle(int x1,int y1,int x2,int y2,int x3,int y3){
            this->x1 = x1;
            this->y1 = y1;
            this->x2 = x2;
            this->y2 = y2;
            this->x3 = x3;
            this->y3 = y3;
           
        }

    // methods for checking the cordinates for first quadrant..
        void validation(){
            if( x1 < 0 || x1 > 30 || y1 < 0 || y1 > 30 || x2 < 0 || x2 > 30 || y2 < 0 || y2 > 30 || x3 < 0 || x3 > 30 || y3 < 0 || y3 > 30){

              
                this->isValidate = 1;
            
            } 
        }
        // method for calculating distances....
        void distance(){
            float a,b,c;
           
            a = sqrt(pow((x2-x1),2) + pow((y2-y1),2) );
            b = sqrt(pow((x3-x2),2) + pow((y3-y2),2) );
            c = sqrt(pow((x3-x1),2) + pow((y3-y1),2) );

            cout<<"length of side a is : "<< a << endl;
            cout<<"length of side b is : "<< b << endl;
            cout<<"length of side c is : "<< c << endl;

          
        }
    // methods for calculating the area...
        void area(){
            
            float a,b,c;
            a = sqrt(pow((x2-x1),2) + pow((y2-y1),2) );
            b = sqrt(pow((x3-x2),2) + pow((y3-y2),2) );
            c = sqrt(pow((x3-x1),2) + pow((y3-y1),2) );

            float s,area;
            s = (a + b + c)/2;
            area = sqrt(s*(s-a)*(s-b)*(s-c));
            cout << "area is : " << area << endl; 
        }


};


int main(){
    // taking cordinates input from the user...
    int x1,y1,x2,y2,x3,y3;
    cout <<"Enter the quardinates in sequence : "<<endl;
    cin >> x1 >> y1 >> x2 >> y2 >> x3 >> y3 ;
  
    //initializing the object of tringle class...
    Tringle t(x1,y1,x2,y2,x3,y3);
    t.validation();

    // validation of object.....
    int isValid = t.isValidate;

    if(isValid == 0){
        t.distance();
        t.area();
    }else{
          cout<<"please enter the correct cordinates..which belonges to first cordinates and not greator than 30"<<endl;
    }

    return 0;
}
