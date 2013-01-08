# -*- encoding: utf-8 -*-
"""
Samples for section 8
"""
from coderunner import *

test(Python30, r"""
print(oct(1000))  #=> '0o1750'
print(0o1750)
print(hex(1000))  #=> '0x3e8'
print(0x3e8)
""", """
0o1750
1000
0x3e8
1000
""")

test(Python27, r"""
print 1 / 2
print 1 // 2
""", """
0
0
""")

test(Python30, r"""
print(1 / 2)
print(1 // 2)
""", """
0.5
0
""")

main()

