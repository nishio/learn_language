import sys
sys.path.insert(0, "../../coderunner")
from coderunner import test, Perl, main

test(Perl, "dynamic.pl", """
yobu-local
""", is_file=True)

test(Perl, "static.pl", """
global
""", is_file=True)

main()
