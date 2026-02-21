#include <iostream>
using namespace std;
int factorial(int f){
    int fact=1;
    for (int i = f; i>=1; i--)
    {
        fact*=i;
    }
    return fact;
}
int coeff(int n,int r){
    int nCr=factorial(n)/(factorial(r)*factorial(n-r));
    return nCr;
}
int main() {
    cout<<coeff(10,3)<<endl;
    return 0;
    
}