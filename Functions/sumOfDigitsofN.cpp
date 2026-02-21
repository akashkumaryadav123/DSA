#include <iostream>
using namespace std;
int sumOfDigits(int n){
    int digsum=0;
    while (n>0)
    {
        int lastdig=n%10;
        n=n/10;
        digsum+=lastdig;
    }
    return digsum;
}
int main() {
    cout<<sumOfDigits(197)<<endl;
    
}