from coderunner import *

header('say Hello in each language')

comment('''
This document was generated from hello.py.
''')

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
console.log("Hello");
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

test(CSharp, r"""
using System;

namespace HelloWorld{
    class Hello{
        static void Main(){
            System.Console.WriteLine("Hello World!");
        }
    }
}
""", """
Hello World!
""")

main()
