#include <iostream>
using namespace std;
bool isPrime(int n){
    if (n<=1)
    {
        return false;
    }
    for (int i = 2; i*i<=n; i++)
    {
        if (n%i==0)
        {
           return false;
        }

        
    }
    return true;
    
    
}
void primeNos(int m){
    for (int  i = 2; i <=m; i++)
    {
       if (isPrime(i))
       {
        cout<<i<<" ";
       }
    }
       
    
}
int main() {
    primeNos(15);
    return 0;
    
}