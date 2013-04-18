int main(){
  int x = 123;
  __asm__("# before if-statement");
  if(x > 0){
    __asm__("# positive");
  }else if(x < 0){
    __asm__("# negative");
  }else{
    __asm__("# zero");
  }
  __asm__("# after if-statement");
}
