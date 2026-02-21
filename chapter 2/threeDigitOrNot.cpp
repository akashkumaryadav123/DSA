#include <iostream>
using namespace std;
int main() {
    int n;
    cout<<"Enter a number : ";
    cin>>n;
    if ((n>99)&&(n<1000))
    {
        cout<<"The number "<<n<<" is three digit";
    }
    else{
        cout<<"The number is not a three digit number";

    }
    
    
}