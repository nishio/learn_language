"""output (checked by coderunner)
* sample of normal process
open: first
open: second
process
close: second
close: first

* sample of failed process() without re-raise
open: first
open: second
process
failed
close with error(<type 'exceptions.RuntimeError'>): second
close: first

* sample of failed process() with re-raise
open: first
open: second
process
failed
close with error(<type 'exceptions.RuntimeError'>): second
close with error(<type 'exceptions.RuntimeError'>): first
Traceback (most recent call last):
  File "with_statement.py", line 64, in <module>
    process(True)
  File "with_statement.py", line 52, in process
    raise RuntimeError
RuntimeError
"""

class MyClass(object):
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print "open: " + self.name

    def __exit__(self, *args):
        if args[0]:
            print "close with error({}): {}".format(args[0], self.name)
        else:
            print "close: " + self.name
        return STOP_EXCEPTION


def process(to_fail):
    with MyClass("first") as x, MyClass("second") as y:
        print "process"
        if to_fail:
            print "failed"
            raise RuntimeError


STOP_EXCEPTION = True
print "* sample of normal process"
process(False)

print "\n* sample of failed process() without re-raise"
process(True)

print "\n* sample of failed process() with re-raise"
STOP_EXCEPTION = False
process(True)
