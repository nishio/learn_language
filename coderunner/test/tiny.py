import sys
sys.path.insert(0, "..")
from coderunner import test, Python, main

test(Python, "print 1", "1")

main()
