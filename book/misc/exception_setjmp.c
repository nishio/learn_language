#include <stdio.h>
#include <setjmp.h>

jmp_buf jbuf;

int shippai(int x){
  printf("%d\n", x);
  if(x == 0){
    longjmp(jbuf, 1);
  }
}

int main(){
  if(!setjmp(jbuf)){
    shippai(1);
    shippai(2); // ここを0に書き換えてみよう
    shippai(3);
  }else{
    printf("Error!\n");
  }
}
