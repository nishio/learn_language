# -*- encoding: utf-8 -*-
import sys
sys.path.insert(0, "../coderunner")
from coderunner import test, Perl, LangC, Python, main

'''
test(Perl, "bless.pl", """
HASH(0x7fe511803ea0)
Counter=HASH(0x7fe511803ea0)
1匹
2匹
""", is_file=True) #TODO: is_embedded_output=True
#TODO HASH(0x7fce6a003ea0) will change its output

test(Perl, "counter.pl", """
HASH(0x7f91a0803ea0)
1匹
Counter=HASH(0x7f91a0803ea0)
2匹
1匹
3匹
""", is_file=True)

test(Perl, "counter_2.pl", """
HASH(0x7fbd3a803ea0)
Counter=HASH(0x7fbd3a803ea0)
1匹
2匹
""", is_file=True)
'''




test(Perl, "counter_1.pl", """
1匹
2匹
1匹
3匹
2匹
""", is_file=True)

test(Perl, "counter_3.pl", """
1匹
1匹
2匹
""", is_file=True)

test(Perl, "dynamic.pl", """
yobu-local
""", is_file=True)

test(Perl, "static.pl", """
global
""", is_file=True)



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

main()
