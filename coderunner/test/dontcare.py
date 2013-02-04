"""
dontcare feature

Following Perl code prints something like "HASH(0x7fc5a9003ea0)" but if changes.
We need to ignore the change.
"""
from coderunner import test, Perl, main


test(Perl, """
$x = {};
print "$x\n";
""", """
HASH(0x7fc5a9003ea0)
""")

main()
