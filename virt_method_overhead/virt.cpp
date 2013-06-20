#include <iostream>
#include <vector>
#include "xbyak/xbyak/xbyak_util.h"

class Bullet{
public:
  virtual void run() = 0;
  void run2(){
    x++;
  }

protected:
  int x;
};

class BulletA : public Bullet{
  void run(){
    x++;
  }
};

class BulletB : public Bullet{
  void run(){
    x++;
  }
};

const int N = 1000;
int main(){
  std::vector<Bullet*> all_bullets;
  std::vector<Bullet*> a_bullets;
  std::vector<Bullet*> b_bullets;

  Bullet* x;
  for(int i=0; i < N; i++){
    if(random() % 2){
      x = new BulletA();
      a_bullets.push_back(x);
    }else{
      x = new BulletB();
      b_bullets.push_back(x);
    }
    all_bullets.push_back(x);
  }


  Xbyak::util::Clock clk1, clk2, clk3;

  for(int i=0; i < 10000; i++){
    for(Bullet* x: all_bullets){
      clk1.begin();
      x->run();
      clk1.end();
    }

    for(Bullet* x: b_bullets){
      clk2.begin();
      x->run();
      clk2.end();
    }
    for(Bullet* x: a_bullets){
      clk2.begin();
      x->run();
      clk2.end();
    }

    for(Bullet* x: all_bullets){
      clk3.begin();
      x->run2();
      clk3.end();
    }
  }
  std::cout << clk1.getClock() << std::endl;
  std::cout << clk2.getClock() << std::endl;
  std::cout << clk3.getClock() << std::endl;
}
