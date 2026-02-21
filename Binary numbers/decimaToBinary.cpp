#include <iostream>
using namespace std;
int main()
{
    int n = 42, reminder, ans = 0;
    int power = 1;
    while (n > 0)
    {
        reminder = n % 2;
        n = n / 2;
        ans += reminder * power;
        power = power * 10;
    }
    cout << ans << " ";

    return 0;
}