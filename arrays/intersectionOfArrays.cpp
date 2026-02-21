#include <iostream>
using namespace std;
void interSecArrays(int arr1[],int arr2[],int sz1,int sz2){
    for (int i = 0; i <sz1; i++)
    {
        for (int j = 0; j < sz2; j++)
        {
            if (arr1[i]==arr2[j])
            {
              cout<<arr1[i]<<" ";
            }
            
        }
        
    }
    

}
int main() {
    int nums1[]={1,2,4,2,14};
    int nums2[]={1,3,4,5,14};
    cout<<"The intersection of two arrays are : ";
    interSecArrays(nums1,nums2,5,5);
    return 0;
    
}