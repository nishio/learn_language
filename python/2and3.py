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
Division
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

"""
Raw Input and Input
"""

test(Python27, """
raw_input("Please enter your name: ")
""", """
Please enter your name: Foo
'Foo'
""")

test(Python30, """
raw_input("Please enter your name: ")
""", """
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    raw_input("Please enter your name: ")
NameError: name 'raw_input' is not defined
""")

test(Python30, """
input("Please enter your name: ")
""", """
Please enter your name: Foo
'Foo'
""")

test(Python27, """
input("Please enter a Python command: ")
""", """
Please enter a Python command: 1+2
3
""")

test(Python30, """
input("Please enter a Python command: ")
""", """
Please enter a Python command: 1+2
'1+2'
""")

test(Python30, """
eval(input("Please enter a Python command: "))
""", """
Please enter a Python command: 1+2
3
""")

"""
Octal Literal is required 0o -- already in Python 2.6
"""

test(Python27, """
print 055
""", """
45
""")

test(Python30, """
print(055)
""", """
SyntaxError: invalid token
""")

test(Python30, """
print(0o55)
""", """
45
""")

"""
long is replaced by int
"""

test(Python27, """
print long(987654321*987654321)
""", """
975461057789971041L
""")

test(Python30, """
print(long(987654321*987654321))
""", """
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    long(987654321*987654321)
NameError: name 'long' is not defined
""")

test(Python30, """
print(int(987654321*987654321))
""", """
975461057789971041
""")

"""
Python 3 strings are Unicode
"""

test(Python27, """
print u"\u0024"
""", """
$
""")

test(Python30, """
print(u"\u0024")
""", """
SyntaxError: invalid syntax
""")

test(Python30, """
print("\u0024")
""", """
$
""")

"""
Builtin basestring abstract type was removed, use str
"""

test(Python27, """
if (isinstance("string", basestring)):
  print "True"
""", """
True
""")

test(Python30, """
if (isinstance("string", basestring)):
  print("True")
""", """
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    isinstance("string", basestring)
NameError: name 'basestring' is not defined
""")

test(Python30, """
if (isinstance("string", str)):
  print("True")
""", """
True
""")

"""
True, False, None are reserved words. 2.6 partially enforced the restrictions on None already
"""

test(Python27, """
True = "True"
""", """
""")

test(Python30, """
True = "True"
""", """
SyntaxError: assignment to keyword
""")

test(Python27, """
False = "False"
""", """
""")

test(Python30, """
False = "False"
""", """
SyntaxError: assignment to keyword
""")

"""
Catching exception
"""

test(Python27, """
try:
  print 1+1
except ValueError, err:
  print err 


""", """
2
""")

test(Python30, """
try:
  print(1+1)
except ValueError, err:

""", """
SyntaxError: invalid syntax
""")

test(Python30, """
try:
  print(1+1)
except ValueError as err:
  print(err)


""", """
2
""")

"""
Tuples need parentheses in comprehensions
"""

test(Python27, """
print [x for x in 1, 2, 3]
""", """
[1, 2, 3]
""")

test(Python30, """
print([x for x in 1, 2, 3])
""", """
SyntaxError: invalid syntax
""")

test(Python30, """
print([x for x in (1, 2, 3)])
""", """
[1, 2, 3]
""")

"""
Remove backtick, use repr()
"""

test(Python27, """
print ''.join([`x` for x in (1,2,3)])
""", """
123
""")

test(Python30, """
print(''.join([`x` for x in (1,2,3)]))
""", """
SyntaxError: invalid syntax
""")

test(Python30, """
print(''.join([repr(x) for x in (1,2,3)]))
""", """
123
""")

"""
Remove <>, use !=
"""

test(Python27, """
print 1 <> 2
""", """
True
""")

test(Python30, """
print(1 <> 2)
""", """
SyntaxError: invalid syntax
""")

test(Python30, """
print(1 != 2)
""", """
True
""")

"""
exec no longer a keyword
"""

test(Python27, """
exec = "exec"
""", """
SyntaxError: invalid syntax
""")

test(Python30, """
exec = "exec"
""", """
""")

"""
The old builtin buffer() is now really gone
"""

test(Python27, """
print buffer("Hello world")
""", """
Hello world
""")

test(Python30, """
print(buffer("Hello world", 6, 5))
""", """
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    buffer("Hello world", 6, 5)
NameError: name 'buffer' is not defined
""")

test(Python30, """
print(memoryview(b"Hello world"))
""", """
<memory at 0x00000000031B68C8>
""")

"""
dictionary's has_key is gone
"""

test(Python27, """
print {"a":1}.has_key("a")
""", """
True
""")

test(Python30, """
print({"a":1}.has_key("a"))
""", """
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    {"a":1}.has_key("a")
AttributeError: 'dict' object has no attribute 'has_key'
""")

test(Python30, """
print("a" in {"a":1})
""", """
True
""")

"""
Some modules were renamed because their old name disobeyed PEP 0008
_winreg --> winreg
ConfigParser --> configparser
copy_reg --> copyreg
Queue --> queue
SocketServer --> socketserver
markupbase --> _markupbase
repr --> reprlib
test.test_support --> test.support
"""

test(Python27, """
import _winreg
""", """
""")

test(Python30, """
_winreg
""", """
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    import _winreg
ImportError: No module named _winreg
""")

test(Python30, """
import winreg
""", """
""")

test(Python27, """
import ConfigParser
""", """
""")

test(Python30, """
ConfigParser
""", """
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    import ConfigParser
ImportError: No module named ConfigParser
""")

test(Python30, """
import configparser
""", """
""")

test(Python27, """
import copy_reg
""", """
""")

test(Python30, """
copy_reg
""", """
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    import copy_reg
ImportError: No module named copy_reg
""")

test(Python30, """
import copyreg
""", """
""")

test(Python27, """
import Queue
""", """
""")

test(Python30, """
Queue
""", """
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    import Queue
ImportError: No module named Queue
""")

test(Python30, """
import queue
""", """
""")

test(Python27, """
import SocketServer
""", """
""")

test(Python30, """
SocketServer
""", """
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    import SocketServer
ImportError: No module named SocketServer
""")

test(Python30, """
import socketserver
""", """
""")

test(Python27, """
import markupbase
""", """
""")

test(Python30, """
markupbase
""", """
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    import markupbase
ImportError: No module named markupbase
""")

test(Python30, """
import _markupbase
""", """
""")

test(Python27, """
import repr
""", """
""")

test(Python30, """
repr
""", """
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    import repr
ImportError: No module named repr
""")

test(Python30, """
import reprlib
""", """
""")

test(Python27, """
import test.test_support
""", """
""")

test(Python30, """
test.test_support
""", """
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    import test.test_support
ImportError: No module named test.test_support
""")

test(Python30, """
import test.support
""", """
""")

"""
string.letters, string.uppercase and string.lowercase is gone
"""

test(Python27, """
import string
string.letters
""", """
'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz\x83\x8a\x8c\x8e\x9a\x9c\x9e\x9f\xaa\xb5\xba\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff'
""")

test(Python30, """
import string
string.letters
""", """
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    string.letters
AttributeError: 'module' object has no attribute 'letters'
""")

test(Python30, """
import string
string.ascii_letters
""", """
'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
""")

test(Python27, """
import string
string.uppercase
""", """
'ABCDEFGHIJKLMNOPQRSTUVWXYZ\x8a\x8c\x8e\x9f\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd8\xd9\xda\xdb\xdc\xdd\xde'
""")

test(Python30, """
import string
string.uppercase
""", """
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    string.uppercase
AttributeError: 'module' object has no attribute 'uppercase'
""")

test(Python30, """
import string
string.ascii_uppercase
""", """
'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
""")

test(Python27, """
import string
string.lowercase
""", """
'abcdefghijklmnopqrstuvwxyz\x83\x9a\x9c\x9e\xaa\xb5\xba\xdf\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff'
""")

test(Python30, """
import string
string.lowercase
""", """
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    string.lowercase
AttributeError: 'module' object has no attribute 'lowercase'
""")

test(Python30, """
import string
string.ascii_lowercase
""", """
'abcdefghijklmnopqrstuvwxyz'
""")

main()
