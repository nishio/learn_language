# -*- encoding: utf-8 -*-
"""
Samples to cause error
"""
from coderunner import test, Python, main

test(Python, """
def good_function():
    global x
    x = 1
""", """
""")

test(Python, """
def bad_function():
    global x = 1
""", """
  File "tmp.py", line 2
    global x = 1
             ^
SyntaxError: invalid syntax
""")

test(Python, """
x = 1
def good_function():
    print x
""", """
""")

test(Python, """
x = 1
def bad_function():
    print x
    x = 2

bad_function()
""", """
Traceback (most recent call last):
  File "tmp.py", line 6, in <module>
    bad_function()
  File "tmp.py", line 3, in bad_function
    print x
UnboundLocalError: local variable 'x' referenced before assignment
""")

test(Python, """
x = 1
def bad_function():
    print x
    global x
    x = 2
""", """
tmp.py:4: SyntaxWarning: name 'x' is used prior to global declaration
  global x
""")

main()
