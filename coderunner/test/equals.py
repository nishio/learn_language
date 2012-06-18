import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from coderunner import *

test(Python, """
print [] == []
""", """
True
""")

test(JS, """
print([] == [])
""", """
false
""")

main()
