#include<iostream>

#define USE_O
#define USE_A
#define USE_B

class O{
#ifdef USE_O
public:
  virtual int f(){
    return 0;
  }
#endif
};

class A : public virtual O{
#ifdef USE_A
public:
  int g(){
    return f();
  }
  /*
  int f(){
    return 1;
  }
  */
#endif
};

class B : virtual public O{
#ifdef USE_B
public:
  int f(){
    return 2;
  }
#endif
};

class C : public A, public B{
};

int main(){
  C c;
  A a = c;
  std::cout << a.g() << std::endl;
}
