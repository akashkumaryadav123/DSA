#include <iostream>
using namespace std;
int main() {
    int n;
    cin>>n;
    int count=0;
    for (int c = 0; c <=n; c++)
    {
        if (c%2!=0)
        {
            count++;
        }
        
    }
    // cout<<count;
    

    for (int i =1; i <=count; i++)
    {
       for (int y = 1; y <=count; y=y+2)
       {
        cout<<"* "<<endl;
       }
       
    }
    
}