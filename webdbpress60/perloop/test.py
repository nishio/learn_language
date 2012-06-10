# -*- encoding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))
from coderunner.coderunner import test, Perl, main

#TODO: is_embedded_output=True
test(Perl, "bless.pl", """
HASH(0x7fe511803ea0)
Counter=HASH(0x7fe511803ea0)
1匹
2匹
""", is_file=True)

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
