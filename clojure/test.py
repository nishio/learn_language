import sys
sys.path.insert(0, "../coderunner")
from coderunner import test, Clojure, main

test(Clojure, "stm.clj", is_file=True, is_embedded_output=True)

main()
