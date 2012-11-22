# -*- encoding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))
from coderunner.coderunner import *



test(Python27, r"""
# -*- encoding: utf-8 -*-
def print_hex(s):
    print " ".join("%x" % ord(c) for c in s)

x = u"aaaああ能aa\\$"

print "JIS"
print_hex(x.encode('iso-2022-jp'))
print "SJIS"
print_hex(x.encode('sjis'))
print "EUC"
print_hex(x.encode('euc-jp'))
""", """

""")


main()

