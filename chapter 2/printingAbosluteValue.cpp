#include <iostream>
using namespace std;
int main() {
    int n;
    cout<<"Enter a number : ";

    cin>>n;
    if(n>=0){
        cout<<"The aboslute value is :"<<n;
    }
    else
    {
        cout<<"the absolute value is: "<<(n=-n);
    }
    

    
}