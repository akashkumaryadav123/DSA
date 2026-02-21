#include<iostream>
#include<vector>
using namespace std;

int main(){
    vector<int>p={1,2,3,4,5};
   
    auto it = p.begin();
    cout<<*(it)<<" "<<endl;
   for(it; it!=p.end();it++){
    cout<<*(it)<<" ";
   }




   return 0;
}