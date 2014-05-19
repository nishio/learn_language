#include <iostream>
#include <signal.h>
#include <setjmp.h>

int err;
jmp_buf env;

void handler(int x){
  std::cout << "Signal " << x << std::endl;
  longjmp(env, x);
}

void division(int denom){
  int result;
  if((err=setjmp(env))){
    result = 12345;
  }else{
    result = 1 / denom;
  }
  std::cout << "1/" << denom << "=" << result << std::endl;
}

int main(int argc, char** argv){
  signal(SIGFPE, handler);
  division(argc); // -> 1/1=1
  division(argc - 1);
  // -> Signal 8
  // -> 1/0=12345
}
