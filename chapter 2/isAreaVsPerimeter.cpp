#include <iostream>
using namespace std;
int main()
{
    float l, b;
    cout << "enter the lenght :";
    cin >> l;
    cout << "enter the breadth :";
    cin >> b;

    if (l * b > 2 * (l + b))
    {
        cout << "the area is greater than perimeter ." << "Area = " << l * b << ">" << "Permimeter ="<<2*(l+b);
    }
    else if (l * b < 2 * (l + b))
    {
        cout << "The perimeter of rectangle is more than the area  " <<"Area ="<< l * b << "<" << "Permimeter =" << 2 * (l + b);
    }
}