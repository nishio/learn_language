#include<iostream>

class MyClass {
public:
  static void my_static_method(){
    std::cout << "I'm static method!" << std::endl;
  }
  void my_instance_method(){
    std::cout << "I'm instance method!" << std::endl;
  }
};

int main(){
  MyClass::my_static_method();
  // -> I'm static method!

  MyClass x;
  x.my_instance_method();
  // -> I'm instance method!
}
