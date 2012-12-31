# -*- encoding: utf-8 -*-
from coderunner import test, Python, main

test(Python, "recursive.py", """
15
""", is_file=True)

main()
