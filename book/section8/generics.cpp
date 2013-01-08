#include <iostream>

template<typename T>
struct person {
  int age;
  char *name;
  T something;
};

int main(){
  person<int> x;
  x.something = 1;
  person<const char*> y;
  y.something = "hoge";

  std::cout << x.something << std::endl; // -> 1
  std::cout << y.something << std::endl; // -> hoge
}
