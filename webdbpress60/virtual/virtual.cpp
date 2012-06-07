/*
  virtualな関数であるかどうかによる挙動の変化
 */

#include<iostream>
using namespace std;
//#define VIRTUAL

class O{
public:
#ifdef VIRTUAL
  virtual 
#endif
  void f(){
    cout << "Base" << endl;
  }
};

class A : public virtual O{
public:
  void g(){
    f();
  }
};

class B : virtual public O{
public:
  void f(){
    cout << "B" << endl;
  }
};

class C : public A, public B{
};

int main(){
  C c;
  c.g(); // when VIRTUAL: B otherwise BASE
  A a = c;
  a.g(); // BASE
}
