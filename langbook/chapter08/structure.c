#include <stdio.h>

struct person {
  int age;
  char *name;
};

int main(){
  struct person x;
  x.name = "nishio";
  x.age = 31;
  printf("%s(%d)\n", x.name, x.age);
}
