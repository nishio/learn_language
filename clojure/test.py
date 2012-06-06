import sys
sys.path.insert(0, "../coderunner")
from coderunner import test, Clojure, main

test(Clojure, "stm.clj", """
start transaction 1
thread t1 opened gate 01
start transaction 2
thread t2 closed gate 21
thread t2 opened gate 02
thread t0 passed the gate 01
thread t0 passed the gate 02
thread t0 opened gate 11 and waiting until gate 03 is open
thread t1 passed the gate 11
modified ref rx: 1
thread t1 opened gate 03
thread t0 passed the gate 03
thread t0 closed gate 02
thread t0 opened gate 21 and waiting until gate 02 is open
thread t2 passed the gate 21
transaction 2 trying to write
start transaction 2
thread t2 closed gate 21
thread t2 opened gate 02
thread t0 passed the gate 02
thread t0 closed gate 02
thread t0 opened gate 21 and waiting until gate 02 is open
thread t2 passed the gate 21
transaction 2 trying to write
start transaction 2
thread t2 closed gate 21
thread t2 opened gate 02
thread t0 passed the gate 02
thread t0 closed gate 02
thread t0 opened gate 12 and waiting until gate 04 is open
thread t1 passed the gate 12
finish transaction 1
thread t1 opened gate 04
thread t0 passed the gate 04
thread t0 opened gate 21 and waiting until gate 02 is open
thread t2 passed the gate 21
transaction 2 trying to write
start transaction 2
thread t2 closed gate 21
thread t2 opened gate 02
thread t0 passed the gate 02
thread t0 opened gate 21 and waiting until gate 02 is open
thread t0 passed the gate 02
thread t0 opened gate 22
thread t2 passed the gate 21
transaction 2 trying to write
modified ref rx: 2
thread t2 passed the gate 22
finish transaction 2
""", is_file=True)

main()
