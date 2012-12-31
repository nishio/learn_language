#include <stdio.h>
int shippai(char* x){
  printf("%s\n", x);
  return 0;
}

int main(){
  if(!shippai("A")){
    printf("Error!\n");
  }else if(!shippai("B")){
    printf("Error!\n");
  }else if(!shippai("C")){
    printf("Error!\n");
  }
}
