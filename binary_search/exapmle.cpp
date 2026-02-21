#include <iostream>
using namespace std;
int binary_search(auto arr,auto target){
    int low =0;
    int high=(sizeof(arr) / sizeof(arr[0]))-1;
    while(low <=high){
        int mid = (low +high)/2;
        int guess=arr[mid];
        if (target ==guess){
            return mid;
        }
        if(guess>target){
           high=mid-1;


        }
        else low =mid +1;


    }
    return 0;
}
int main(){
    int myNumbers[]={1,2,3,4,5,6,7};
    cout<<(binary_search(myNumbers,5));
    return 0;
}

