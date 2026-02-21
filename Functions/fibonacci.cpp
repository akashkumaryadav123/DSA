#include <iostream>
using namespace std;
void fibonacci(int n)
{
    int t1 = 0, t2 = 1, f = 0;
    if (n == 1)
    {
        cout << t1 << " ";
    }
    else if (n == 2)
    {
        cout << t2;
    }
    else
    {
        for (int i = 3; i <= n; i++)
        {

            f = t1 + t2;
            t1 = t2;
            t2 = f;

            cout << f << " ";
        }
    }
}
int main()
{
    fibonacci(10);
    return 0;
}