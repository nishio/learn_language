int main(){
  float x = 3.0, y = 7.0, z;
  int i = 3, j = 7, k;
  __asm__("#hoge");
  z = x + y;
  __asm__("#fuga");
  k = i + j;
  __asm__("#fuga");
}
