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
    if ((a+b)>c&&(b+c)>a&&(c+a)>b&&a!=0&&b!=0&&c!=0)
    {
       cout<<"The entered numbers can be the sides of triangle.";
    }
    else
    {
        cout<<"The entered numbers cannot be the sides of triangle";
    }
    
    
}