from coderunner import *

test(Python, """
print 1 / 0
""", """
Traceback (most recent call last):
  File "tmp.py", line 1, in <module>
    print 1 / 0
ZeroDivisionError: integer division or modulo by zero
""")


test(Ruby, r"""
puts 1 / 0
""","""
tmp.rb:1:in `/': divided by 0 (ZeroDivisionError)
	from tmp.rb:1:in `<main>'
""")


test(JS, r"""
console.log(1 / 0);
""","""
Infinity
""")


test(Perl, r"""
print 1 / 0;
""","""
Illegal division by zero at tmp.pl line 1.
""")


test(Java, r"""
public class Tmp {
    public static void main(String[] args){
        System.out.println(1 / 0);
    }
}
""","""
Exception in thread "main" java.lang.ArithmeticException: / by zero
	at Tmp.main(Tmp.java:3)
""")


test(Cpp, r"""
#include <stdio.h>
int main(){
  printf("%d\n", 1 / 0);
}
""","""
tmp.cpp: In function 'int main()':
tmp.cpp:3: warning: division by zero in '1 / 0'
""", to_run=False)


test(Clojure, """
(print (/ 1 0))
""", """
Exception in thread "main" java.lang.ArithmeticException: Divide by zero
	at clojure.lang.Numbers.divide(Numbers.java:156)
	at clojure.lang.Numbers.divide(Numbers.java:3691)
	at user$eval1.invoke(tmp.clj:1)
	at clojure.lang.Compiler.eval(Compiler.java:6511)
	at clojure.lang.Compiler.load(Compiler.java:6952)
	at clojure.lang.Compiler.loadFile(Compiler.java:6912)
	at clojure.main$load_script.invoke(main.clj:283)
	at clojure.main$script_opt.invoke(main.clj:343)
	at clojure.main$main.doInvoke(main.clj:427)
	at clojure.lang.RestFn.invoke(RestFn.java:408)
	at clojure.lang.Var.invoke(Var.java:415)
	at clojure.lang.AFn.applyToHelper(AFn.java:161)
	at clojure.lang.Var.applyTo(Var.java:532)
	at clojure.main.main(main.java:37)
""")

test(Scheme, r"""
(display (/ 1 0))
""", """
+inf.0
""")

test(Smalltalk, """
1 / 0
""", """
ZeroDivide: 
""")

main()
