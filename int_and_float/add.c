// Sample code to read same binary value as int and float
// thanks: Dragan Zivkovic

#include <stdio.h>
#include <assert.h>
#include <stdlib.h>
#include <string.h>

void show(float x)
{
  unsigned int i;
  unsigned int j;
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
  printf("  %g as float\n", x);
  printf("  %u as uint\n\n", i);
}

int main(int argc, char *argv[])
{
  float x = 3.0, y = 7.0;
  unsigned int ix = 0, iy = 0;

  assert(sizeof(float) == 4);
  assert(sizeof(unsigned int) == 4);

  show(x);
  show(y);

  printf("Add as float:\n");
  show(x + y);

  printf("Add as integer:\n");
  memcpy(&ix, &x, sizeof(ix));
  memcpy(&iy, &y, sizeof(ix));
  ix += iy; // add as integer
  memcpy(&x, &ix, sizeof(ix));
  show(x);

  return 0;
}

/* output (checked by coderunner)
Hexadecimal value 0x40400000 in memory,
  01000000010000000000000000000000 as binary,
  3 as float
  1077936128 as uint

Hexadecimal value 0x40E00000 in memory,
  01000000111000000000000000000000 as binary,
  7 as float
  1088421888 as uint

Add as float:
Hexadecimal value 0x41200000 in memory,
  01000001001000000000000000000000 as binary,
  10 as float
  1092616192 as uint

Add as integer:
Hexadecimal value 0x81200000 in memory,
  10000001001000000000000000000000 as binary,
  -2.93874e-38 as float
  2166358016 as uint
 */
