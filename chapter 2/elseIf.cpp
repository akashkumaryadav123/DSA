#include <iostream>
using namespace std;
int main() {
    float cp,sp;
    cout<<"The cost price is : ";
    cin>>cp;
    cout<<"The sellng price is : ";
    cin>>sp;
    if (sp>cp)
    {
      cout<<"The seller made profit of "<<sp-cp<<endl;
      cout<<"The percentage profit made was : "<<(sp-cp)/cp*100;
    }
    else if(sp<cp){
        cout<<"The seller made loss of : "<<cp-sp<<endl;
        cout<<"The percentage loss made was : "<<(cp-sp)/cp*100;

    }
    else if(cp==sp){
        cout<<"No profit or loss was made";
    }
    
}