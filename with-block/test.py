# -*- encoding: utf-8 -*-
"""
Test of similar feature
- Python's with-statement
- Java7's try-with-resource
- C#'s using-statement
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from coderunner.coderunner import test, Python, Java7, CSharp, main

test(Java7, "TryWithResource.java", is_file=True, is_embedded_output=True)
test(CSharp, "Using.cs", is_file=True, is_embedded_output=True)
test(Python, "with_statement.py", is_file=True, is_embedded_output=True)

main()
