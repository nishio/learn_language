// Sample code to read same binary value as int and float
// thanks: Dragan Zivkovic

#include <stdio.h>
#include <assert.h>
#include <stdlib.h>
#include <string.h>

void show(float x)
{
  unsigned int i;
  int j;
  memcpy(&i, &x, sizeof(i));
  char s[33];
  s[32] = '\0';
  for(j = 0; j < 32; j++) {
    if((i >> j) & 1) {
      s[31 - j] = '1';
    } else {
      s[31 - j] = '0';
    }
  }
  printf("Hexadecimal value 0x%X in memory,\n", i);
  printf("  %s as binary,\n", s);
  printf("  %f as float\n", x);
  printf("  %d as unsigned int\n", i);
}

int main(int argc, char *argv[])
{
  assert(sizeof(float) == 4);
  assert(sizeof(unsigned int) == 4);
  show(0.0);
  show(1.0);
  show(2.0);
  show(1.5);
  show(-0.0);
  show(1.0 / 0.0);
  show(-1.0 / 0.0);
  show(0.0 / 0.0);
  return 0;
}
