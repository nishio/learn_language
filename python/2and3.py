# -*- encoding: utf-8 -*-
"""
Different betwern Python2.* and Python3.*
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from coderunner.coderunner import test, Python27, Python30, main

"""
Print Is A Function
"""

test(Python27, """
print "hello"
""", """
hello
""")

test(Python30, """
print "hello"
""", """
  File "tmp.py", line 1
    print "hello"
                ^
SyntaxError: invalid syntax
""")

test(Python30, """
print("hello")
""", """
hello
""")


"""
Views And Iterators Instead Of Lists
"""

test(Python27, """
print {}.keys()
""", """
[]
""")

test(Python30, """
print({}.keys())
""", """
<dict_keys object at 0x385f50>
""")


"""
Ordering Comparisons
"""

test(Python27, """
print None < None
""", """
False
""")

test(Python30, """
print(None < None)
""", """
Traceback (most recent call last):
  File "tmp.py", line 1, in <module>
    print(None < None)
TypeError: unorderable types: NoneType() < NoneType()
""")

"""
Ordering Comparisons
"""

test(Python27, """
print 1 / 2
""", """
0
""")

test(Python30, """
print(1 / 2)
""", """
0.5
""")

main()
