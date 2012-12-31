import sys
sys.path.insert(0, "..")
from code_runner import test, Cpp, main

test(Cpp, "raii.cpp", """
scenario1: normal case
try to open
open
try to use
use
close


scenario2: failed to open
try to open
throw
exception caught: error on open


scenario3: opened, but failed to use
try to open
open
try to use
throw
close
exception caught: error on use
""", is_file=True)

main()
