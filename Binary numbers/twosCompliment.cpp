#include <iostream>
using namespace std;
int deciBinary(int n){
  int reminder,power=1,ans=0;
  while (n>0)
  {
    reminder=n%2;
    n=n/2;
    ans+=(reminder*power);
    power*=10;

  }
  return ans;
  
}
int main() {
  /*steps for two's compliment example(-8)
  1)convert no to binary
  2)add prefix 0 infront of the binary no.
  3)flip the binary no 1-0 & 0-1
  4)add +1 to the flipped no.
  */
  int binary= deciBinary(8);
  int prefix=0;//cannot be added because memory does not identifies 0 prefix before number as integer
  int flip;
  return 0;

    

    
}