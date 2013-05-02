from coderunner import *

test(Python, """
print 1.7976931348623157e+308
""", """
1.79769313486e+308
""")

test(Ruby, """
print 1.7976931348623157e+308
""", """
1.7976931348623157e+308
""")

test(Perl, """
print 1.7976931348623157e+308
""", """
inf
""")

test(JS, """
console.log(1.7976931348623157e+308)
""", """
1.7976931348623157e+308
""")

test(LangC, r"""
#include<stdio.h>
int main(){
  printf("%f\n", 1.7976931348623157e+308);
}
""", """
179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368.000000
""")

test(Java, r"""
public class Tmp {
    public static void main(String[] args){
        System.out.println(1.7976931348623157e+308);
    }
}
""","""
1.7976931348623157E308
""")

test(Scheme, r"""
(display 1.7976931348623157e+308)
""", """
1.7976931348623157e308
""")

test(CSharp, r"""
using System;

namespace HelloWorld{
    class Hello{
        static void Main(){
            System.Console.WriteLine(1.7976931348623157e+308);
        }
    }
}
""", """
1.79769313486232E+308
""")

test(CommonLisp, r"""
(print 1.7976931348623157e+308)
""", """
*** - 
      SYSTEM::LPAR-READER: floating point overflow
""")


main()
