import sys
sys.path.insert(0, "../coderunner")
from coderunner import test, Perl, LangC, main

#test(Perl, "bless.pl", is_file=True, is_embedded_output=True)
test(LangC, "for.c", """
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

main()
