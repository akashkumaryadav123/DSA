#include <iostream>
using namespace std;
int main() {
    int size=5;
    int arr[size]={1,3,5,9,2};
    cout<<"Before reversing : "<<endl;
     for (int i = 0; i <size; i++)
    {
        cout<<arr[i]<<" ";
    }
    for (int i = 0; i <size/2; i++)
    {
        swap(arr[i],arr[size-1-i]);
    }
     cout<<"After reversing : "<<endl;
    for (int i = 0; i <size; i++)
    {
        cout<<arr[i]<<" ";
    }
    return 0;
    
    
}