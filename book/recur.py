# -*- coding: utf-8 -*-
def is_integer(x):
    return isinstance(x, int)

def total(xs):
    result = 0
    for x in xs:
        if is_integer(x):
            result += x
        else:
            pass # ...

    return result

def total(xs):
    result = 0
    for x in xs:
        if is_integer(x):
            result += x
        else:
            # xはリストなのでfor文で回す
            for y in x:
                if is_integer(y):
                    result += y
                else:
                    pass # さらにリストが来たらどうすればいいんだ？

    return result

def total(xs):
    result = 0
    for x in xs:
        if is_integer(x):
            result += x
        else:
            result += total(x)

    return result

print total([1, 2, [3, 4], 5])
print total([1, 2, [3, [4, 5]]])
