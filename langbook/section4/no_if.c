#include <stdio.h>
void use_if(int x){
  if(x > 0){
    printf("正の数\n");
  }else if(x < 0){
    printf("負の数\n");
  }else{
    printf("ゼロ\n");
  }
}

void not_use_if(int x){
  if(x <= 0) goto NOT_POSITIVE;
  printf("正の数\n");
  goto END;
 NOT_POSITIVE:
  if(x >= 0) goto NOT_NEGATIVE;
  printf("負の数\n");
  goto END;
 NOT_NEGATIVE:
  printf("ゼロ\n");
 END:
  return;
}

int main(){
  use_if(-1);
  use_if(0);
  use_if(1);
  not_use_if(-1);
  not_use_if(0);
  not_use_if(1);
}
