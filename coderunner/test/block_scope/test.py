from coderunner import *

comment('''
Python and JS don't have block scope
''')


test(Python, """
try:
    x = 'ok'
finally:
    print x
""", """
ok
""")


test(JS, """
try{
    x = 'ok';
}finally{
    console.log(x);
}
""", """
ok
""")


test(Java, """
public class Tmp {
    public static void main(String[] args){
        try{
            String x = "ok";
        }finally{
            System.out.println(x);
        }
    }
}
""", """
Tmp.java:6: error: cannot find symbol
            System.out.println(x);
                               ^
  symbol:   variable x
  location: class Tmp
1 error
""", to_run=False)

test(Cpp, "forscope.cpp", """
3
""", is_file=True, extra_option=['-fno-for-scope'])

test(Cpp, "forscope.cpp", """
forscope.cpp: In function 'int main()':
forscope.cpp:6: error: name lookup of 'i' changed for new ISO 'for' scoping
forscope.cpp:4: error:   using obsolete binding at 'i'
""", is_file=True, to_run=False)


main()
