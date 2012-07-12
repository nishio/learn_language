# -*- encoding: utf-8 -*-
"""

"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from coderunner.coderunner import test, Python, Java7, CSharp, main

test(Python, """
class Foo(object):
    def __enter__(self):
        print "open"

    def __exit__(self, *args):
        print "close", args


with Foo() as x:
    print "normal process"


print


with Foo() as x:
    print "error occured"
    1/0
""", """
open
normal process
close (None, None, None)

open
error occured
close (<type 'exceptions.ZeroDivisionError'>, ZeroDivisionError('integer division or modulo by zero',), <traceback object at ..dontcare..>)
Traceback (most recent call last):
  File "tmp.py", line 18, in <module>
    1/0
ZeroDivisionError: integer division or modulo by zero
""")

test(Python, """
class Foo(object):
    def __enter__(self):
        print "open"

    def __exit__(self, *args):
        print "close", args
        return True # stop exception


with Foo() as x:
    print "error occured"
    1/0
""", """
open
error occured
close (<type 'exceptions.ZeroDivisionError'>, ZeroDivisionError('integer division or modulo by zero',), <traceback object at ..dontcare..>)
""")

test(Java7, "TryWithResource.java", is_file=True, is_embedded_output=True)

main()
