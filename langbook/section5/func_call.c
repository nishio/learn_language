int foo(){
  __asm__("#called");
  return 1;
}

int main(){
  __asm__("#call");
  return foo();
}
