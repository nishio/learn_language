import sys
sys.path.insert(0, "../coderunner")
from coderunner import test, LangC, main

test(LangC, "main.c", """
Hexadecimal value 0x40500000 in memory, read as integer variable is 1078984704
Hexadecimal value 0x40500000 in memory, read as float variable is 3.250000
""", is_file=True)


test(LangC, "float_as_int.c", """
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
""", is_file=True)

main()
