# -*- encoding: utf-8 -*-
import sys
sys.path.insert(0, "../../coderunner")
from coderunner import test, LangC, Java, main

test(LangC, "no_for.c", """
use_for
0
1
2
3
4
not_use_for
0
1
2
3
4
""", is_file=True)

test(LangC, "no_while.c", """
use_while
5
4
3
2
1
not_use_while
5
4
3
2
1
""", is_file=True)

test(LangC, "no_if.c", """
負の数
ゼロ
正の数
負の数
ゼロ
正の数
""", is_file=True)

test(Java, "SyntaxTest.java", """
C style for-loop
1
2
3
4
5
Iterator for-loop
1
2
3
4
5
For-each loop
1
2
3
4
5
""", is_file=True)

main()
