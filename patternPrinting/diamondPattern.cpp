#include <iostream>
using namespace std;
int main() {
    int n=4;
    for (int i = 0; i<n; i++)
    {
     for (int j =n-i-1; j>=0; j--)
     {
        cout<<" ";

     }
     for (int k=1; k<=i+1; k++)
     {
        cout<<k;
     }
     for (int l = i; l>=1; l--)
     {
      cout<<l;
     }
     
     
     cout<<endl;
     
    }
    for (int m =n; m>=0; m--)
    {
     for (int o =0; o<=n-m-1; o++)
     {
        cout<<" ";

     }
     for (int p=1; p<=m+1; p++)
     {
        cout<<p;
     }
     for (int q = m; q>=1; q--)
     {
      cout<<q;
     }
     
     
     cout<<endl;
     
    }

    
    
}