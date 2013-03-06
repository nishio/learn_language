from coderunner import test, Clojure, main

test(Clojure, "stm.clj", is_file=True, is_embedded_output=True)
test(Clojure, "stm2.clj", is_file=True, is_embedded_output=True)
test(Clojure, "var.clj", is_file=True, is_embedded_output=True)
test(Clojure, "atom.clj", is_file=True, is_embedded_output=True)

main()
