# -*- coding: utf-8 -*-
'''
code runner: tools to run small codes (sample code of documents)

# USAGE: register tests with 'test' func, then call 'main'

test(Python,
"""
1/0
""",
"""
Traceback (most recent call last):
  File "tmp.py", line 1, in <module>
    1/0
ZeroDivisionError: integer division or modulo by zero
""")

test(Java,
"exception.java", is_file=True, to_run=False)
'''
import subprocess
import os
STOP_ON_MISMATCH = True
tests = []


class Test(object):
    def subproc(self, cmd):
        p = subprocess.Popen(
            cmd,
            stderr=subprocess.STDOUT,
            stdout=subprocess.PIPE)
        ret, _dummy = p.communicate("")
        ret = ret.strip("\n")
        return ret

    def check_expect(self, ret):
        """
        check whether ret == self.expect and show if not.
        """
        if ret != self.expect:
            print
            print "ERROR"
            print "code " + "=" * 35
            print self.code
            print "expected " + "=" * 31
            print self.expect
            print "got " + "=" * 36
            print ret
            print "=" * 40
            if STOP_ON_MISMATCH:
                raise AssertionError

    def show(self):
        """
        show code. currently output ReST (for my book)
        """
        print "::"
        print
        print indent(self.comment)
        print indent(self.code)
        print "  " + "-" * 20
        print indent(self.expect)
        print "\n"

    def __init__(self, code, expect="", is_file=False, to_run=True):
        """
        is_file: when code is large you can put it in the other file
        to_run: when you want to compile, but not want to run
                (especially Java, C++)
        """
        if is_file:
            self.filename = code
            assert os.path.isfile(code), "2nd arg must be filename"
            self.code = file(code).read()
            self.is_file = True
        else:
            self.filename = self.temp_filename
            self.code = code.strip("\n")
            self.is_file = False
        self.expect = expect.strip("\n")
        self.to_run = to_run


class TestScript(Test):
    def run(self):
        if not self.is_file:
            file(self.filename, "w").write(self.code)

        ret = self.subproc(self.bin.split() + [self.filename])
        self.check_expect(ret)


class Python27(TestScript):
    bin = "python2.7"
    comment = "# Python2.7"
    temp_filename = "tmp.py"


class Python(Python27):
    comment = "# Python"


class Ruby18(TestScript):
    bin = "ruby1.8"
    comment = "# Ruby1.8"
    temp_filename = "tmp.rb"


class Ruby19(TestScript):
    bin = "ruby1.9"
    comment = "# Ruby1.9"
    temp_filename = "tmp.rb"


class Ruby(Ruby19):
    comment = "# Ruby"


class NodeJS(TestScript):
    bin = "node"
    comment = "// Node.js"
    temp_filename = "tmp.js"


class Rhino(TestScript):
    bin = "rhino"
    comment = "// Rhino"
    temp_filename = "tmp.js"


class JS(Rhino):
    comment = "// JS"


class Perl5(TestScript):
    bin = "perl5"
    comment = "# Perl5"
    temp_filename = "tmp.pl"


class Perl(Perl5):
    comment = "# Perl"


class Clojure(TestScript):
    bin = "java -cp clojure-1.4.0.jar:. clojure.main"
    temp_filename = "tmp.clj"
    comment = "// Clojure"


class Java(Test):
    comment = "// Java"
    temp_filename = "Tmp.java"

    def run(self):
        if not self.is_file:
            file(self.filename, "w").write(self.code)

        ret = self.subproc(
            ["env", "LC_ALL=en", "javac", self.filename])
        if self.to_run:
            trunk = self.filename.replace(".java", "")
            ret += self.subproc(
                ["env", "LC_ALL=en", "java", "-cp", ".", trunk])
        self.check_expect(ret)


class LangC(Test):
    comment = "/* C */"
    temp_filename = "tmp.c"

    def run(self):
        if not self.is_file:
            file(self.filename, "w").write(self.code)

        cmd = ("gcc").split() + [self.filename]
        ret = self.subproc(cmd)
        if self.to_run:
            ret += self.subproc(["env", "./a.out"])
        self.check_expect(ret)


class Cpp(Test):
    comment = "// C++"
    temp_filename = "tmp.cpp"

    def run(self):
        if self.is_file:
            file(self.filename, "w").write(self.code)

        cmd = ("g++ -Wall -W -Wformat=2 -Wcast-qual -Wcast-align "
               "-Wwrite-strings -Wconversion -Wfloat-equal "
               "-Wpointer-arith -Woverloaded-virtual -Wnon-virtual-dtor "
               "-I/opt/local/include/ -O3").split() + [self.filename]
        ret = self.subproc(cmd)
        if self.to_run:
            ret += self.subproc(["env", "./a.out"])
        self.check_expect(ret)


def test(lang, *args, **kw):
    "register tests"
    tests.append(
        lang(*args, **kw))


def run_tests():
    for test in tests:
        test.run()


def indent(s):
    return "\n".join("  " + line for line in s.split("\n"))


def show_tests():
    for test in tests:
        test.show()


def main():
    # TODO: use optparse to choose run/show test
    run_tests()
    show_tests()

if __name__ == "__main__":
    main()
