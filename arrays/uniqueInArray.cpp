#include <iostream>
using namespace std;
void unique(int arr[],int sz)
{
    
    for (int i = 0; i < sz; i++)
    {
        int j=0;
        while (j<sz)
        {
           if (arr[i]^arr[j])
           {
            
           }
           
        }
        
        
       

    }
}
int main()
{
    int nums[] = {1, 2, 3, 1, 4, 3};
    cout << "the unique elements are : ";
    unique(nums,6);
    return 0;
}
  

