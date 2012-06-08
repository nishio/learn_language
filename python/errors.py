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
def foo(x=0, **kw):
    print x, kw

foo(1, x=2)
""", """
Traceback (most recent call last):
  File "tmp.py", line 4, in <module>
    foo(1, x=2)
TypeError: foo() got multiple values for keyword argument 'x'
""")

main()
