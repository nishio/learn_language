/* It write 16384 bytes again and again on 1MB disk,
 * then fprintf become to fail and return -1.
 */
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]){
  char s[1024 * 16];
  int i;
  for(i = 0; i < 1024 * 16; i++){
    s[i] = 'A';
  }
  s[1024 * 16 - 1] = '\0';

  FILE* fp = fopen("/ramcache/t.txt", "w");
  for(i = 0; i < 64; i++){
    int ret = fprintf(fp, "%s\n", s);
    printf("%d\n", ret);
  }
  fclose(fp);
}
