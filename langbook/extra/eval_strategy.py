def foo(x):
    print "foo"
    return x + 1

def bar(x):
    print "bar"
    return x * 2

print foo(bar(1))
