import sys
sys.path.insert(0, "..")
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


main()
