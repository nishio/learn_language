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
  show(1.75);
  show(3.5);
  show(7);
  show(-0.0);
  show(1.0 / 0.0);
  show(-1.0 / 0.0);
  show(0.0 / 0.0);
  return 0;
}

/* output (checked by coderunner)
Hexadecimal value 0x0 in memory,
  00000000000000000000000000000000 as binary,
  0.000000 as float
  0 as unsigned int
Hexadecimal value 0x3F800000 in memory,
  00111111100000000000000000000000 as binary,
  1.000000 as float
  1065353216 as unsigned int
Hexadecimal value 0x40000000 in memory,
  01000000000000000000000000000000 as binary,
  2.000000 as float
  1073741824 as unsigned int
Hexadecimal value 0x3FC00000 in memory,
  00111111110000000000000000000000 as binary,
  1.500000 as float
  1069547520 as unsigned int
Hexadecimal value 0x3FE00000 in memory,
  00111111111000000000000000000000 as binary,
  1.750000 as float
  1071644672 as unsigned int
Hexadecimal value 0x40600000 in memory,
  01000000011000000000000000000000 as binary,
  3.500000 as float
  1080033280 as unsigned int
Hexadecimal value 0x40E00000 in memory,
  01000000111000000000000000000000 as binary,
  7.000000 as float
  1088421888 as unsigned int
Hexadecimal value 0x80000000 in memory,
  10000000000000000000000000000000 as binary,
  -0.000000 as float
  -2147483648 as unsigned int
Hexadecimal value 0x7F800000 in memory,
  01111111100000000000000000000000 as binary,
  inf as float
  2139095040 as unsigned int
Hexadecimal value 0xFF800000 in memory,
  11111111100000000000000000000000 as binary,
  -inf as float
  -8388608 as unsigned int
Hexadecimal value 0x7FC00000 in memory,
  01111111110000000000000000000000 as binary,
  nan as float
  2143289344 as unsigned int
 */
