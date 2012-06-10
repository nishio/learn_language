import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from coderunner import *

test(Python, """
print 1 / 2
""", """
0
""")

test(Python, """
from __future__ import division
print 1 / 2
""", """
0.5
""")


test(Ruby, r"""
puts 1 / 2
""","""
0
""")


test(JS, r"""
print(1 / 2);
""","""
0.5
""")


test(Perl, r"""
print 1 / 2;
""","""
0.5
""")


test(Java, r"""
public class Tmp {
    public static void main(String[] args){
        System.out.println(1 / 2);
    }
}
""","""
0
""")


test(Cpp, r"""
#include <stdio.h>
int main(){
  printf("%d\n", 1 / 2);
}
""","""
0
""")


test(Clojure, """
(print (/ 1 2))
""", """
1/2
""")

test(Scheme, r"""
(display (/ 1 2))
""", """
1/2
""")

main()
