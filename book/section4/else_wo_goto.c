#include<stdio.h>

int main(){
  int x = -10;
  if(x > 0){
    printf("正の数\n");
  }else if(x < 0){
    printf("負の数\n");
  }else{
    printf("ゼロ\n");
  }
}
