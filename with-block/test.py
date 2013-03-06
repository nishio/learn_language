# -*- encoding: utf-8 -*-
"""
Test of similar feature
- Python's with-statement
- Java7's try-with-resource
- C#'s using-statement
"""
from coderunner import test, Python, Java7, CSharp, main

test(Java7, "TryWithResource.java", is_file=True, is_embedded_output=True)
test(CSharp, "Using.cs", is_file=True, is_embedded_output=True)
test(Python, "with_statement.py", is_file=True, is_embedded_output=True)
test(Python, "with_statement2.py", is_file=True, is_embedded_output=True)


main()
