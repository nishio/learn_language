# -*- encoding: utf-8 -*-
"""
Sample codes for section 3
"""
from coderunner import *

test(Ruby, """
if 0 then
  print "true!"
else
  print "false!"
end
""", """
true!
""")

test(LangC, r"""
#include <stdio.h>

int main(){
  if(0){
    printf("true!\n");
  }else{
    printf("false!\n");
  }
}
""", """
false!
""")

main()
