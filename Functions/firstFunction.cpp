// #include <iostream>
// using namespace std;
// int sum(int a,int b){
//     int result;
//     result=a+b;
//     return result;
// }
// int main() {
//   int num1,num2;
//   cin>>num1>>num2;
//   cout<<sum(num1,num2);
//   return 0;

// }
#include <iostream>
using namespace std;
int sum(int a, int b)
{
    int result = a + b;
    return result;
}
int main()
{
    int num1, num2;
    cin >> num1 >> num2;
    cout << sum(num1, num2);
    return 0;
}