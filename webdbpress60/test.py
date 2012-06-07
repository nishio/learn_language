# -*- encoding: utf-8 -*-
import sys
sys.path.insert(0, "../coderunner")
from coderunner import test, Perl, LangC, Python, Ruby, main


test(Ruby, "module_inheritance.rb", """
hello
hello
""", is_file=True)

test(Ruby, "mixin.rb", """
bar!
""", is_file=True)

test(Perl, "reenter.pl", """
0
""", is_file=True)

test(Python, "oldclass.py", """
base
D2
base
""", is_file=True)


test(LangC, "syntax/no_for.c", """
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

test(LangC, "syntax/no_while.c", """
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

test(LangC, "syntax/no_if.c", """
負の数
ゼロ
正の数
負の数
ゼロ
正の数
""", is_file=True)

main()
