// Sample code to read same binary value as int and float
// thanks: Dragan Zivkovic

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[])
{
  // int value in 32bit width memory
  unsigned int a = 0;
  // float value in 32bit width memory
  float b = 0;

  // set hexadecimal (binary) value in memory
  a = 0x40500000;
  // print value from memory as integer
  printf("Hexadecimal value 0x%X in memory, read as integer variable is %d\n", a, a);
  // copy hexadecimal (binary) value from integer variable a to float variable b
  memcpy(&b, &a, sizeof(a));
  // print variable b as float
  printf("Hexadecimal value 0x%X in memory, read as float variable is %f\n", a, b);

  return 0;
}
