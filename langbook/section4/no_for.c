#include <stdio.h>

void use_for(){
  printf("use_for\n");
  int N = 5;
  int i;
  for(i = 0; i < N; i++){
    printf("%d\n", i);
  }
}

void not_use_for(){
  printf("not_use_for\n");
  int N = 5;
  int i;
  i = 0;
  while(i < N){
    printf("%d\n", i);
    i++;
  }
}

int main(int argc, char** argv){
  use_for();
  not_use_for();
}


