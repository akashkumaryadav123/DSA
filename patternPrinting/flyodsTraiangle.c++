#include <iostream>
using namespace std;
int main() {
    int n=3;
    char ch=65;
    for (int i = 0; i <n; i++)
    {
     for (int j =0; j<=i; j++)
     {
        cout<<" ";

     }
     for (int k = 0; k<n-i; k++)
     {
        cout<<ch;
        
     }
     ch++;
     
     cout<<endl;
     
     
    }
    
}