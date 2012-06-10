import sys
sys.path.insert(0, "../coderunner")
from coderunner import test, LangC, main

test(LangC, "main.c", is_file=True, is_embedded_output=True)
test(LangC, "float_as_int.c", is_file=True, is_embedded_output=True)
test(LangC, "add.c", is_file=True, is_embedded_output=True)

main()
