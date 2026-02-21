#include <iostream>
using namespace std;
int main()
{
    int n = 5;
    int arr[5] = {1,4,2,4,3};
    for(int st=0;st<n;st++){
        for (int end =st; end <n;end++)
        {
            for(int i=st;i<=end;i++){
                cout<<arr[i];
            }
            cout<<" ";

        }
        cout<<endl;
        
    }
    return 0;
}