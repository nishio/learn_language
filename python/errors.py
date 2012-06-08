# -*- encoding: utf-8 -*-
"""
Samples to cause error
"""
import sys
sys.path.insert(0, "../coderunner")
from coderunner import test, Python, main

test(Python, """
if true:
print 1
""", """
  File "tmp.py", line 2
    print 1
        ^
IndentationError: expected an indented block
""")

test(Python, """
if true:
    print 1
   print 2
""", """
  File "tmp.py", line 3
    print 2
          ^
IndentationError: unindent does not match any outer indentation level
""")

test(Python, """
# -*- encoding: utf-8 -*-
if true:
　print 1 # unicode space character
""", """
  File "tmp.py", line 3
    　print 1 # unicode space character
    ^
SyntaxError: invalid syntax
""")

test(Python, """
print "こんにちは"
""", r"""
  File "tmp.py", line 1
SyntaxError: Non-ASCII character '\xe3' in file tmp.py on line 1, but no encoding declared; see http://www.python.org/peps/pep-0263.html for details
""")

test(Python, """
# -*- encoding: utf-8 -*-
print "こんにちは"
""", """
こんにちは
""")

test(Python, """
def foo(): pass

foo(1)
""", """
Traceback (most recent call last):
  File "tmp.py", line 3, in <module>
    foo(1)
TypeError: foo() takes no arguments (1 given)
""")

test(Python, """
def foo(x=1): pass

foo(y=1)
""", """
Traceback (most recent call last):
  File "tmp.py", line 3, in <module>
    foo(y=1)
TypeError: foo() got an unexpected keyword argument 'y'
""")

test(Python, """
def foo(x, y, z=0): pass

foo(1, z=1)
""", """
Traceback (most recent call last):
  File "tmp.py", line 3, in <module>
    foo(1, z=1)
TypeError: foo() takes at least 2 arguments (2 given)
""")

test(Python, """
def foo(x=0, **kw):
    print x, kw

foo(1, x=2)
""", """
Traceback (most recent call last):
  File "tmp.py", line 4, in <module>
    foo(1, x=2)
TypeError: foo() got multiple values for keyword argument 'x'
""")

test(Python, """
''[0]
""", """
Traceback (most recent call last):
  File "tmp.py", line 1, in <module>
    ''[0]
IndexError: string index out of range
""")

test(Python, """
'' + 0
""", """
Traceback (most recent call last):
  File "tmp.py", line 1, in <module>
    '' + 0
TypeError: cannot concatenate 'str' and 'int' objects
""")

test(Python, """
0 + ''
""", """
Traceback (most recent call last):
  File "tmp.py", line 1, in <module>
    0 + ''
TypeError: unsupported operand type(s) for +: 'int' and 'str'
""")

test(Python, """
-''
""", """
Traceback (most recent call last):
  File "tmp.py", line 1, in <module>
    -''
TypeError: bad operand type for unary -: 'str'
""")

test(Python, """
x
""", """
Traceback (most recent call last):
  File "tmp.py", line 1, in <module>
    x
NameError: name 'x' is not defined
""")

test(Python, r"""
u'' + '\xFF'
""", r"""
Traceback (most recent call last):
  File "tmp.py", line 1, in <module>
    u'' + '\xFF'
UnicodeDecodeError: 'ascii' codec can't decode byte 0xff in position 0: ordinal not in range(128)
""")

test(Python, r"""
{}['x']
""", """
Traceback (most recent call last):
  File "tmp.py", line 1, in <module>
    {}['x']
KeyError: 'x'
""")

test(Python, r"""
[].x
""", """
Traceback (most recent call last):
  File "tmp.py", line 1, in <module>
    [].x
AttributeError: 'list' object has no attribute 'x'
""")

test(Python, r"""
import x
""", """
Traceback (most recent call last):
  File "tmp.py", line 1, in <module>
    import x
ImportError: No module named x
""")

main()
