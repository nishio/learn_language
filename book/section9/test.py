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
JIS
61 61 61 1b 24 42 24 22 24 22 47 3d 1b 28 42 61 61 5c 24
SJIS
61 61 61 82 a0 82 a0 94 5c 61 61 5c 24
EUC
61 61 61 a4 a2 a4 a2 c7 bd 61 61 5c 24
""")

test(Python27, r"""
# -*- encoding: utf-8 -*-
def print_hex(s):
    print " ".join("%x" % ord(c) for c in s)

x = u"aaaあああaaa"

print "JIS"
print_hex(x.encode('iso-2022-jp'))
print "SJIS"
print_hex(x.encode('sjis'))
print "EUC"
print_hex(x.encode('euc-jp'))
""", """
JIS
61 61 61 1b 24 42 24 22 24 22 24 22 1b 28 42 61 61 61
SJIS
61 61 61 82 a0 82 a0 82 a0 61 61 61
EUC
61 61 61 a4 a2 a4 a2 a4 a2 61 61 61
""")


test(Python27, r"""
# -*- encoding: utf-8 -*-
print '$"$"$"'.decode('iso-2022-jp')
print '\x1b$B$"$"$"'.decode('iso-2022-jp').encode('utf-8')
""", """
$"$"$"
あああ
""")


test(Python27, r"""
# 日本語でコメントを書いただけ
""", r"""
  File "tmp.py", line 1
SyntaxError: Non-ASCII character '\xe6' in file tmp.py on line 1, but no encoding declared; see http://www.python.org/peps/pep-0263.html for details
""")

test(Python27, r"""
# -*- encoding: utf-8 -*-

# 日本語でコメントを書いただけ
""", """
""")

main()

