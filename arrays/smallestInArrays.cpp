#include <iostream>
using namespace std;
int main() {
    int size =5;
    int marks[size];
    for (int i = 0; i <size; i++)
    {
        cin>>marks[i];
    }
    int min=marks[0];
    for (int i = 1; i <size; i++)
    {
        if (marks[i]<min)
        {
           min=marks[i];
        }
        
    }
    cout<<"min : "<<min<<endl;
}