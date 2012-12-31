#include <stdio.h>
int shippai(char* x){
  printf("%s\n", x);
  return 0;
}

int main(){
  if(!shippai("A")) goto ERROR;
  if(!shippai("B")) goto ERROR;
  if(!shippai("C")) goto ERROR;
  return;
ERROR:
  printf("Error!\n");
}
