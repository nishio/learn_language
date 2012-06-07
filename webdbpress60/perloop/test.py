# -*- encoding: utf-8 -*-
import sys
sys.path.insert(0, "../../coderunner")
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

test(Perl, "inherit.pl", """
Bar=HASH(0x7fd981810a90)
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

test(Perl, "pack.pl", """
スズメ: 1匹
スズメ: 2匹
スズメ: 3匹
スズメ: リセット
スズメ: 1匹
""", is_file=True)

test(Perl, "pack2.pl", """
スズメ: 1匹
スズメ: 2匹
スズメ: 3匹
スズメ: リセット
スズメ: 4匹
""", is_file=True)



main()
