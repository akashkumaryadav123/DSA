#include <iostream>
using namespace std;
int sum(int N){
    int result = 0;
    for (int i = 1; i <=N; i++)
    {
        result=result+i;
    }
    return result;
    
}
int main() {
    cout<<sum(10);
    return 0;
}