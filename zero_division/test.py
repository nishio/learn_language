# -*- encoding: utf-8 -*-
"""
Trap zero division error
"""
from coderunner import test, Cpp, main

test(Cpp, "zero_division.cpp", is_file=True, is_embedded_output=True, ignore_warning=True)

main()
