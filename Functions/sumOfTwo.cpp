#include <iostream>
using namespace std;
int main()
{
    int n, target;
    cout << "Enter length of arr: ";
    cin >> n;
    cout << "Enter the target: ";
    cin >> target;
    int arr[n];
    for (int i = 0; i < n; i++)
    {
        cout << "Enter the element of arr " << i << " : ";
        cin >> arr[i];
    }
    int a, b;
    for (int i = 0; i < n; i++)
    {
        a = arr[i];
        for (int j = i + 1; j < n; j++)
        {

            b = arr[j];
            if (a + b == target)
            {
               cout << "Pair found: " << arr[i] << ", " << arr[j] << endl;
            }
        }
    }
}