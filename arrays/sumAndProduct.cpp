#include <iostream>
using namespace std;
int sumOfElements(int arr[], int sz)
{
    int sum = 0;
    for (int i = 0; i < sz; i++)
    {
        sum = sum + arr[i];
    }
    return sum;
}
int prodOfElements(int arr[], int sz)
{
    int prod = 1;
    for (int i = 0; i < sz; i++)
    {
        prod *= arr[i];
    }
    return prod;
}
// sum
int main()
{
    int sz = 5;
    int arr[sz] = {1, 3, 2, 5, 2};
    cout << "The sum of elements of the array is " << sumOfElements(arr, sz) << endl;

    cout << "The product of elements of the array is " << prodOfElements(arr, sz) << endl;
    return 0;
}