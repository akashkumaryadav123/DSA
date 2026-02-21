#include <iostream>
using namespace std;
int main() {
    int size=5;
    int num[size];
    cout<<"Enter the elements of the arrays : "<<endl;
    for (int  i = 0; i <size; i++)
    {
        cin>>num[i];
    }
    int max=num[0];
    for (int i = 1; i <size; i++)
    {
        if (num[i]>max)
        {
            max=num[i];
        }
        
    }
    cout<<"The max in the array is : "<<max<<endl;
    return 0;
    
    
}