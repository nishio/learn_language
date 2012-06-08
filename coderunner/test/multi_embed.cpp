#include <stdio.h>

int main(){
  printf("hello!\n"); //-> hello!
  printf("hello!\n"); //-> hello!
  for(int i=0; i < 5; i++){
    printf("%d\n", i);
  }
}

/* output (checked by coderunner)
0
1
2
3
4
 */
