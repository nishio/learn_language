#include <stdio.h>
void use_while(int x){
  printf("use_while\n");
  while(x > 0){
    printf("%d\n", x);
    x--;
  }
}

void not_use_while(int x){
  printf("not_use_while\n");
 START_LOOP:
  if(!(x > 0)) goto END_LOOP;
  printf("%d\n", x);
  x--;
  goto START_LOOP;
 END_LOOP:
  return;
}

int main(){
  use_while(5);
  not_use_while(5);
}
