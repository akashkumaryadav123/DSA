#include <iostream>
using namespace std;
void swapAlternate(int arr[],int n){
    if (n%2==0)
    {
        for (int i = 0; i <n; i=i+2)
        {
           swap(arr[i],arr[i+1]);
    
        }     
    }
    else
    {
        for (int i = 0; i <n-1; i=i+2)
        {
           swap(arr[i],arr[i+1]);
    
        }    
        
    }
    
    
    

}
int main() {
    
    int students[]={2,4,6,3,9,10,8};
    int size=sizeof(students)/sizeof(students[0]);
    swapAlternate(students,size);
    for (int i = 0; i <size; i++)
    {
        cout<<students[i]<<" ";
    }
    
    return 0;
    
}