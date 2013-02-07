from coderunner import *

test(JS, """
x = [1, 10, 2, 100]
x.sort()
console.log(x)
""", """
[ 1, 10, 100, 2 ]
""")

"""
https://developer.mozilla.org/en-US/docs/JavaScript/Reference/Global_Objects/Array/sort
> Sorts the elements of an array in place and returns the array.

> If compareFunction is not supplied, elements are sorted by converting them to strings and comparing strings in lexicographic ("dictionary" or "telephone book," not numerical) order. For example, "80" comes before "9" in lexicographic order, but in a numeric sort 9 comes before 80.
"""

test(Python, """
x = [1, 10, 2, 100]
x.sort()
print x
""", """
[1, 2, 10, 100]
""")


test(JS, """
// replace first match
console.log("abcabc".replace("b", "!"))

// replace all match
console.log("abcabc".replace(/b/g, "!"))
""", """
a!cabc
a!ca!c
""")

test(Python, """
# replace all match
print "abcabc".replace("b", "!")

# replace first match
print "abcabc".replace("b", "!", 1)
""", """
a!ca!c
a!cabc
""")

test(JS, """
console.log(1 % 3)
console.log(1 % -3)
console.log(-1 % 3)
console.log(-1 % -3)
console.log(1 / 3)
console.log(1 / -3)
""", """
1
1
-1
-1
0.3333333333333333
-0.3333333333333333
""")

test(Python, """
print 1 % 3
print 1 % -3
print -1 % 3
print -1 % -3
print 1 / 3
print 1 / -3
""", """
1
-2
2
-1
0
-1
""")

test(Python30, """
print(1 % 3)
print(1 % -3)
print(-1 % 3)
print(-1 % -3)
print(1 / 3)
print(1 / -3)
""", """
1
-2
2
-1
0.333333333333
-0.333333333333
""")

test(JS, """
$ = 1
""")

test(Python, """
$ = 1
""", """
  File "tmp.py", line 1
    $ = 1
    ^
SyntaxError: invalid syntax
""")

test(JS, """
console.log("1 2 3 4".split())
console.log("1 2 3 4".split(" ", 2))
""", """
[ '1 2 3 4' ]
[ '1', '2' ]
""")

test(Python, """
print "1 2 3 4".split()
print "1 2 3 4".split(" ", 2)
""", """
['1', '2', '3', '4']
['1', '2', '3 4']
""")

test(JS, """
console.log("abc".split(""))
""", """
[ 'a', 'b', 'c' ]
""")

test(Python, """
print "abc".split("")
""", """
Traceback (most recent call last):
  File "tmp.py", line 1, in <module>
    print "abc".split("")
ValueError: empty separator
""")

test(Python, """
print list("abc")
""", """
['a', 'b', 'c']
""")


test(JS, """
console.log(0x20000000000000 == 0x20000000000001)
console.log(0x20000000000000)
console.log(0x20000000000000 + 1)
console.log(0x20000000000000 + 892800745259009)
console.log(0x20000000000000 + 892800745259009 + 1)
""", """
true
9007199254740992
9007199254740992
9900000000000000
9900000000000000
""")

test(Python, """
print 0x20000000000000 == 0x20000000000001
print 0x20000000000000
print 0x20000000000000 + 1
print 0x20000000000000 + 892800745259008
print 0x20000000000000 + 892800745259008 + 1
""", """
False
9007199254740992
9007199254740993
9900000000000000
9900000000000001
""")

test(JS, """
a = function b(){console.log(b)}
console.log(a)
a()
console.log(b) //-> error
""", """
[Function: b]
[Function: b]

node.js:201
        throw e; // process.nextTick error, or 'error' event on first tick
              ^
ReferenceError: b is not defined
    at Object.<anonymous> (/home/nishio/learn_language/coderunner/tmp.js:4:13)
    at Module._compile (module.js:441:26)
    at Object..js (module.js:459:10)
    at Module.load (module.js:348:32)
    at Function._load (module.js:308:12)
    at Array.0 (module.js:479:10)
    at EventEmitter._tickCallback (node.js:192:41)
""")

main()
