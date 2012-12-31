"""output (checked by coderunner)
init False
enter False
init True
exit False <type 'exceptions.RuntimeError'>
Traceback (most recent call last):
  File "with_statement2.py", line 27, in <module>
    with Foo(False) as x, Foo(True) as y:
  File "with_statement2.py", line 19, in __init__
    raise RuntimeError
RuntimeError
"""

class Foo(object):
    def __init__(self, to_fail):
        print "init", to_fail
        self.to_fail = to_fail
        if to_fail:
            raise RuntimeError

    def __enter__(self):
        print "enter", self.to_fail

    def __exit__(self, *args):
        print "exit", self.to_fail, args[0]

with Foo(False) as x, Foo(True) as y:
    print "Hello"

