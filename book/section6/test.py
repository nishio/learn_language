# -*- encoding: utf-8 -*-
"""
Samples to cause error
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))
from coderunner.coderunner import *


test(Python, """
def foo(x, y):
  print x, y

foo(1)
""", """
Traceback (most recent call last):
  File "tmp.py", line 4, in <module>
    foo(1)
TypeError: foo() takes exactly 2 arguments (1 given)
""")

test(Ruby, """
def foo(x, y)
  p x, y
end

foo 1
""", """
tmp.rb:1:in `foo': wrong number of arguments (1 for 2) (ArgumentError)
	from tmp.rb:5:in `<main>'
""")

test(JS, """
function foo(x, y){
  print(x, y);
}

foo(1)
""", """
1 undefined
""")



test(Python, """
x = [0, 1, 2]
print x[3]
""", """
Traceback (most recent call last):
  File "tmp.py", line 2, in <module>
    print x[3]
IndexError: list index out of range
""")

test(Ruby, """
x = [0, 1, 2]
p x[3]
""", """
nil
""")

test(JS, """
x = [0, 1, 2]
print(x[3])
""", """
undefined
""")

main()

