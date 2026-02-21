#include <iostream>
using namespace std;
int main() {
    int size=5;
    int arr[size]={1,2,4,3,27};
    cout<<"Before reversing Array : "<<endl;
    for (int i = 0; i <size; i++)
    {
        cout<<"arr ["<<i<<"] : "<<arr[i]<<endl;
    }
    for (int i = 0; i <size/2; i++)
    {
        int rev=arr[i];
        arr[i]=arr[size-1-i];
       arr[size-1-i]=rev;

        
    }
    cout<<"After reversing the array : "<<endl;
    for (int i = 0; i <size; i++)
    {
       cout<<"arr ["<<i<<"] : "<<arr[i]<<endl;
    }
    return 0;
    

    
    
}
