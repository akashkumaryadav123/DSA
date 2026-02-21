#include <iostream>
using namespace std;
int main()
{
    int n = 1010;
    int power = 1;
    int digsum=0;
    while (n>0)
    {
        int lastdig=n%10;
        n=n/10;
        digsum+=(lastdig*power);
        power*=2;
    }
    cout << digsum;

    return 0;
}