#include<stdio.h>

int main(){
  int x = -10;
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
