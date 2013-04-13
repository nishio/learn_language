#include <stdio.h>

int add_one(int x){
  return x + 1;
}

int main(){
  printf("%d\n", add_one(100)); /* -> 101 */
}
