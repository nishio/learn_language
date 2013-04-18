#include <stdio.h>

int add_int(){
  int x = 1, ret;
  __asm__("# before add int");
  ret = x + 1024;
  __asm__("# after add int");
  return ret;
}

float add_float(){
  float x = 1.0, ret;
  __asm__("# before add float");
  ret = x + 1024;
  __asm__("# after add float");
  return ret;
}

float divide_int(int x){
  return x / 2;
}

float divide_float(float x){
  return x / 2;
}

int main(){
  printf("%f\n", divide_int(1));
  printf("%f\n", divide_float(1));
}
