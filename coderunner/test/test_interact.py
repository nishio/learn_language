from coderunner import *

test(GHCi, r"""
:t 1
:t \x -> x
""", r"""
Prelude> :t 1
1 :: (Num t) => t
Prelude> :t \x -> x
\x -> x :: t -> t
""")

test(Prolog, r"""
1 = 2.
1 = 1.
1 = X.
member(X, [1, 2]).
;
""","""
?- 1 = 2.
false.

?- 1 = 1.
true.

?- 1 = X.
X = 1.

?- member(X, [1, 2]).
X = 1 ;
X = 2.
""")

test(ScalaInteractive, r"""
1
""","""
scala> 1
res0: Int = 1
""")

main()
