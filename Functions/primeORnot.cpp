#include <iostream>
using namespace std;

bool isPrime(int a)
{
    if (a <= 1)
    {
       return false;
    }
    for (int i = 2; i * i <= a; i++)
    {
        if (a% i == 0)
        {
            return false;
        }
    }
   
    
       return true;
    
}

int main()
{
    if (isPrime(11))
    {
        cout<<"Prime number\n";
    }
    else{
        cout<<"Not a prime number\n";
    }
    
    return 0;
}