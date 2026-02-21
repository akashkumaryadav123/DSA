#include <iostream>
using namespace std;
int min(int a,int b){
    if (a>b)
    {
        return b;
    }
    else{
       return a;
    }
    
    
}
int main() {
    int num1,num2;
    cin>>num1>>num2;
    cout<<min(num1,num2);
    return 0;
    
}