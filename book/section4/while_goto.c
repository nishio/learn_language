#include <stdio.h>

int main(){
  int x = 5;
 START_LOOP:
  if(!(x > 0)) goto END_LOOP;
  printf("%d\n", x);
  x--;
  goto START_LOOP;
 END_LOOP:
  ;
}
