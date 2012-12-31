from code_runner import test, main, Python, Ruby, JS

# arguments number mismatch
test(Python, """
def foo(x, y): print y

foo(1)
""", """
Traceback (most recent call last):
  File "tmp.py", line 3, in <module>
    foo(1)
TypeError: foo() takes exactly 2 arguments (1 given)
""")

test(Ruby, """
def foo(x, y)
  p y
end

foo(1)
""", """
tmp.rb:1:in `foo': wrong number of arguments (1 for 2) (ArgumentError)
	from tmp.rb:5:in `<main>'
""")

test(JS, """
function foo(x, y){
  print(y);
}

foo(1)
""", """
undefined
""")

# range error
test(Python, """
print [0, 1, 2][3]
""", """
Traceback (most recent call last):
  File "tmp.py", line 1, in <module>
    print [0, 1, 2][3]
IndexError: list index out of range
""")

test(Ruby, """
p [0, 1, 2][3]
""", """
nil
""")


test(JS, """
print([0, 1, 2][3])
""", """
undefined
""")

main()
