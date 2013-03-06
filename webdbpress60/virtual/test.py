from coderunner import test, Cpp, main

test(Cpp, "virtual.cpp", """
Base
Base
""", is_file=True)
test(Cpp, "virtual.cpp", """
B
Base
""", is_file=True, extra_option=["-DVIRTUAL"])

main()
