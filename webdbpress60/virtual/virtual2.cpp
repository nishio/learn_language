#include<iostream>

using namespace std;

class Base {
public:
  virtual void f(){
    cout << "Base" << endl;
  }
};

class D1 : virtual public Base {
public:
  void f(){
    cout << "D1" << endl;
  }
};

int main(){
  Base b;
  b.f();
}

