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

test(Python, r"""
int("a")
""", """
Traceback (most recent call last):
  File "tmp.py", line 1, in <module>
    int("a")
ValueError: invalid literal for int() with base 10: 'a'
""")

test(Python, r"""
"%s %s %s" % (1, 2)
""", """
Traceback (most recent call last):
  File "tmp.py", line 1, in <module>
    "%s %s %s" % (1, 2)
TypeError: not enough arguments for format string
""")

test(Python, r"""
"%s %s" % [1, 2]
""", """
Traceback (most recent call last):
  File "tmp.py", line 1, in <module>
    "%s %s" % [1, 2]
TypeError: not enough arguments for format string
""")

test(Python, r"""
1 / 0
""", """
Traceback (most recent call last):
  File "tmp.py", line 1, in <module>
    1 / 0
ZeroDivisionError: integer division or modulo by zero
""")

test(Python, r"""
def foo():
    return

foo() + 1
""", """
Traceback (most recent call last):
  File "tmp.py", line 4, in <module>
    foo() + 1
TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'
""")

test(Python, r"""
class Foo(object):
    def say(self):
        pass

Foo.say()
""", """
Traceback (most recent call last):
  File "tmp.py", line 5, in <module>
    Foo.say()
TypeError: unbound method say() must be called with Foo instance as first argument (got nothing instead)
""")

test(Python, r"""
class A(object): pass
class B(object): pass
class AB(A, B): pass
class BA(B, A): pass
class C(AB, BA): pass
""", """
Traceback (most recent call last):
  File "tmp.py", line 5, in <module>
    class C(AB, BA): pass
TypeError: Error when calling the metaclass bases
    Cannot create a consistent method resolution
order (MRO) for bases B, A
""")

test(Python, """
def func(a=[]):
    a.append(1)
    return a

print func()
print func()
print func()
""", """
[1]
[1, 1]
[1, 1, 1]
""")

test(Python, """
def f():
    print "called"

def func(x=f()):
    pass
""", """
called
""")

test(Python, """
# assignment in bar doesn't affect outside
def foo():
    x = 0
    def bar():
        x = 1

    bar()
    print x

foo()
""", """
0
""")

test(Python, """
# list comprehension doesn't make scope
funcs = [(lambda: x) for x in range(3)]
print funcs[0]()
print funcs[1]()
""", """
2
2
""")

test(Python, """
x = 0
def foo():
    x += 1

foo()
""", """
Traceback (most recent call last):
  File "tmp.py", line 5, in <module>
    foo()
  File "tmp.py", line 3, in foo
    x += 1
UnboundLocalError: local variable 'x' referenced before assignment
""")

test(Python, """
x = 0
def foo():
    global x
    x += 1

foo()
print x
""", """
1
""")


test(Python, """
# class variable is not a global variable
class Foo(object):
    x = 1
    def foo(self):
        print x

Foo().foo()
""", """
Traceback (most recent call last):
  File "tmp.py", line 7, in <module>
    Foo().foo()
  File "tmp.py", line 5, in foo
    print x
NameError: global name 'x' is not defined
""")

test(Python, """
class Foo(object):
    x = 1
    def foo(self):
        print self.x

Foo().foo()
""", """
1
""")

test(Python, """
# class variable is shared by instances
class Foo(object):
    x = []
    def foo(self):
        self.x.append(1)
        print self.x

Foo().foo()
Foo().foo()
""", """
[1]
[1, 1]
""")

test(Python, """
def foo(a=1, b): pass
""", """
  File "tmp.py", line 1
    def foo(a=1, b): pass
SyntaxError: non-default argument follows default argument
""")

test(Python, """
def foo(a=1, b): pass
""", """
  File "tmp.py", line 1
    def foo(a=1, b): pass
SyntaxError: non-default argument follows default argument
""")

test(Python, """
object.a = 1
""", """
Traceback (most recent call last):
  File "tmp.py", line 1, in <module>
    object.a = 1
TypeError: can't set attributes of built-in/extension type 'object'
""")


main()


