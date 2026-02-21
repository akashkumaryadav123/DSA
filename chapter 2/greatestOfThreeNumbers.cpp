#include <iostream>
using namespace std;
int main() {
    int a,b,c;
    cout<<"Enter a :";
    cin>>a;
    cout<<"Enter b :";
    cin>>b;
    cout<<"Enter c :";
    cin>>c;
    if(a>b&&a>c){
        cout<<a<<" is greatest";
    }
    else if(b>a&&b>c){
        cout<<b<<" is greatest";
    }
    else if(c>b&&c>a){
        cout<<c<<" is greatest";
    }
    else if (a=b=c){
        cout<<"All are equal";
    }
    else if ((a=b=c)==0){
        cout<<"All are equal to 0";
    }
}