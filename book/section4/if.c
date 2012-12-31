int main(){
  int x = 123;
  __asm__("# before if-statement");
  if(x == 456){
    __asm__("# in if-statement");
  }
  __asm__("# after if-statement");
}
