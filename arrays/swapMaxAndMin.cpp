#include <iostream>
using namespace std;
void swapMaxAndMin(int arr[], int size)
{

    int max = arr[0];
    for (int i = 1; i < size; i++)
    {
        if (arr[i] > max)
            max = arr[i];
    }

    int min = arr[0];
    for (int i = 1; i < size; i++)
    {
        if (arr[i] < min)
        {
            min = arr[i];
        }
    }
    int s1, s2;
    for (int i = 0; i < size; i++)
    {
        if (max == arr[i])
        {
           s1 = i;
        }
    }
    for (int i = 0; i < size; i++)
    {
        if (min == arr[i])
        {
            s2 = i;
        }
    }
    
     swap(arr[s1], arr[s2]);
}
int main()
{
    int count = 5;
    int nums[count] = {1, 24, 23, 28, -6};
    swapMaxAndMin(nums, count);
    for (int i = 0; i < count; i++)
    {
        cout<<nums[i]<<" ";
    }
    
    return 0;
}