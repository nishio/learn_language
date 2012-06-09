import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from coderunner import *

test(Python, """
print "Hello"
""", """
Hello
""")


test(Ruby, r"""
puts "Hello"
""","""
Hello
""")


test(JS, r"""
print("Hello");
""","""
Hello
""")


test(Perl, r"""
print "Hello\n";
""","""
Hello
""")


test(Java, r"""
public class Tmp {
    public static void main(String[] args){
        System.out.println("Hello");
    }
}
""","""
Hello
""")


test(Cpp, r"""
#include <stdio.h>
int main(){
  printf("Hello\n");
}
""","""
Hello
""")


test(Clojure, """
(print "Hello")
""", """
Hello
""")

test(Scheme, r"""
(display "Hello")
""", """
Hello
""")

main()
