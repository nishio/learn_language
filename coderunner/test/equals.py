from coderunner import *

test(Python, """
print [] == []
""", """
True
""")

test(JS, """
console.log([] == [])
""", """
false
""")

main()
