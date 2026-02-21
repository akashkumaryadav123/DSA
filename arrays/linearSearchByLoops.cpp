#include <iostream>
using namespace std;
int main() {
    int size=5;
    int nums[size];
    for (int i = 0; i <size; i++)
    {
        cout<<"Enter the Nums["<<i<<"] : ";
        cin>>nums[i];
    }
    int target = 8;
    for (int i = 0; i < size; i++)
    {
        if(nums[i]==target){
            cout<<"Yes,terget found in array at num["<<i<<"]"<<endl;
        }
    }
    return 0;
    
    
    
}