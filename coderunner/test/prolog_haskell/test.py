from coderunner import *

test(Haskell, """
foo 0 = do{ print "rule1"; print 0 }
foo n = do{ print "rule2"; print n }

main = do
  foo (1 - 1)
  foo 1
  foo 0
""", """
"rule1"
0
"rule2"
1
"rule1"
0
""")

test(Prolog, r"""
1 = 2.
1 = 1.
1 = X.
member(X, [1, 2]).
;
""","""
?- [tmp].
% tmp compiled 0.00 sec, 3 clauses
true.

?- 1 = 2.
false.

?- 1 = 1.
true.

?- 1 = X.
X = 1.

?- member(X, [1, 2]).
X = 1 ;
X = 2.
""").with_module('tmp', """
foo(0) :- print('rule1: '), print(0).
foo(N) :- print('rule2: '), print(N).
""")

main()
