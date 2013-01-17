from coderunner import *

test(Python, """
x, y = 1, 2, 3
""", """
Traceback (most recent call last):
  File "tmp.py", line 1, in <module>
    x, y = 1, 2, 3
ValueError: too many values to unpack
""")

test(Python, """
x, y, z = 1, 2
""", """
Traceback (most recent call last):
  File "tmp.py", line 1, in <module>
    x, y, z = 1, 2
ValueError: need more than 2 values to unpack
""")

test(Ruby, """
x, y = 1, 2, 3
p x
p y
""", """
1
2
""")
test(Ruby, """
x, y, z = 1, 2
p x
p y
p z
""", """
1
2
nil
""")

main()
