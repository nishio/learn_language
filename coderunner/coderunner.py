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
import argparse
import subprocess
import difflib
import os
import re

tests = []
BIN_PATH = os.path.join(os.path.abspath(
        os.path.dirname(__file__)), 'bin')
PATH = ":".join([BIN_PATH] + os.environ.get('PATH', '').split(":"))

def _indent(s):
    r"""
    >>> _indent("aaa")
    '  aaa'
    >>> _indent("aaa\nbbb")
    '  aaa\n  bbb'
    """
    return "\n".join("  " + line for line in s.split("\n"))


def _pattern(prefix, body, suffix):
    """
    generate regular pattern, which match with
    *body* sandwiched between *prefix* and *suffix*
    but not include *prefix* and *suffix*.

    >>> _pattern("<", "([^>]+)", ">")
    '(?<=<)([^>]+)(?=>)'

    >>> re.findall(_, "aa<abc>de<foo>bar")
    ['abc', 'foo']
    """
    pre = "(?<=%s)" % prefix  # positive lookbehind assertion
    suf = "(?=%s)" % suffix  # lookahead assertion
    return pre + body + suf


def _multi_pattern(*patterns):
    """
    combine multiple rgular expression
    >>> _multi_pattern("(A+)", "(B+)")
    '(?:(A+)|(B+))'
    >>> re.findall(_, "AAABBBAAA")
    [('AAA', ''), ('', 'BBB'), ('AAA', '')]
    """
    return "(?:%s)" % "|".join(patterns)


class Test(object):
    """
    embedded_output_pattern:
      regular expression to find output desctiption

    dontcare_pattern:
      regular expression to ignore part of output
    """
    embedded_output_pattern = None
    dontcare_pattern = None
    pygments_name = 'none'

    def subproc(self, cmd):
        p = subprocess.Popen(
            cmd,
            stderr=subprocess.STDOUT,
            stdout=subprocess.PIPE,
            env={"PATH": PATH})
        ret, _dummy = p.communicate("")
        ret = ret.strip("\n")
        return ret

    def check_expect(self, ret):
        """
        check whether ret == self.expect and show if not.
        """
        if self.dontcare_pattern:
            self.expect = re.sub(
                self.dontcare_pattern,
                "..dontcare..", self.expect)
            ret = re.sub(
                self.dontcare_pattern,
                "..dontcare..", ret)

        if ret != self.expect:
            print
            print "ERROR"
            if self.is_file:
                print "file:", self.filename
            else:
                print "code " + "=" * 35
                print self.code
                print "=" * 40

            expectlines = self.expect.split("\n")
            gotlines = ret.split("\n")
            difflines = list(difflib.unified_diff(
                    expectlines, gotlines, "expected", "got"))
            if len(difflines) < len(expectlines) + len(gotlines):
                print "diff " + "=" * 35
                print "\n".join(difflines)
                print "=" * 40
            else:
                print "expected " + "=" * 31
                print self.expect
                print "got " + "=" * 36
                print ret
                print "=" * 40
            if not args.nonstop:
                if args.copy_got_output:
                    # TODO: support other OS (now Mac only)
                    p = subprocess.Popen(["pbcopy"], stdin=subprocess.PIPE)
                    p.stdin.write(ret)
                    p.stdin.close()
                raise AssertionError

    def show(self):
        if args.format == "rest":
            self.show_in_rest()
        elif args.format == "mybook":
            self.show_for_mybook()
        else:
            raise NotImplementedError

    def show_in_rest(self):
        """
        show code. currently output ReST (for my book)
        """
        if args.lang_format == "strong":
            print "**%s**" % self.human_name
        elif args.lang_format == "none":
            pass # print nothing
        else: # default: "heading"
            print self.human_name
            print "=" * len(self.human_name)

        print
        print ".. code-block:: %s" % self.pygments_name
        print
        print _indent(self.code.strip("\n"))
        if not args.suppress_expected:
            expected = self.expect.strip("\n")
            if expected == "": expected = "(no output)"
            print
            print "::"
            print
            print _indent(expected)
        print "\n"

    def show_for_mybook(self):
        """
        show code. currently output ReST (for my book)
        """
        print "::"
        print
        print _indent(self.code.strip("\n"))
        print _indent("-" * 20)
        print _indent(self.expect.strip("\n"))
        print "\n"

    def __init__(self, code, expect="", is_file=False,
                 to_run=True, is_embedded_output=False):
        """
        is_file: when code is large you can put it in the other file
        to_run: False when you don't want to run
                (especially in Java, C++, you may want to check
                 the code fail to compile)
        is_embedded_output: whether output is embedded in the given code
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

        if is_embedded_output:
            assert is_file
            if not self.embedded_output_pattern:
                raise NotImplementedError
            self.expect = self.get_embedded_output()
            pat = re.compile(self.embedded_output_pattern, re.DOTALL)
            self.code = re.sub(
                pat, "", self.code).strip("\n")
        else:
            self.expect = expect.strip("\n")

        self.to_run = to_run

    def get_embedded_output(self):
        data = file(self.filename).read()
        pat = re.compile(self.embedded_output_pattern, re.DOTALL)
        buf = []
        for match in re.findall(pat, data):
            if isinstance(match, str):
                buf.append(match.strip("\n"))
            else:
                for group in match:
                    if group: # not empty string
                        buf.append(group.strip("\n"))

        assert buf, "no embedded output found"
        return "\n".join(buf)



class TestScript(Test):
    def run(self):
        if not self.is_file:
            file(self.filename, "w").write(self.code)

        ret = self.subproc(self.bin.split() + [self.filename])
        self.check_expect(ret)


class _Python(TestScript):
    pygments_name = "python"
    temp_filename = "tmp.py"
    dontcare_pattern = _pattern(r" at ", "0x[0-9a-fX]+", r">")


class Python27(_Python):
    bin = "python2.7"
    human_name = "Python2.7"


class Python30(_Python):
    bin = "python3.0"
    human_name = "Python3.0"


class Python(Python27):
    human_name = "Python"


class _Ruby(TestScript):
    temp_filename = "tmp.rb"
    pygments_name = "ruby"


class Ruby18(_Ruby):
    bin = "ruby1.8"
    human_name = "Ruby1.8"


class Ruby19(_Ruby):
    bin = "ruby1.9"
    human_name = "Ruby1.9"


class Ruby(Ruby19):
    human_name = "Ruby"


class _JS(TestScript):
    temp_filename = "tmp.js"
    pygments_name = "javascript"

class NodeJS(_JS):
    bin = "node"
    human_name = "Node.js"


class Rhino(_JS):
    bin = "rhino"
    human_name = "Rhino"


class JS(Rhino):
    human_name = "JavaScript"


class _Perl(TestScript):
    temp_filename = "tmp.pl"
    dontcare_pattern = _pattern(r"HASH\(", "0x[0-9a-fX]+", r"\)")
    pygments_name = "perl"

class Perl5(_Perl):
    bin = "perl5"
    human_name = "Perl5"


class Perl(Perl5):
    human_name = "Perl"


_clojure_path = os.path.join(
    os.path.dirname(__file__),
    'bin', 'clojure-1.4.0.jar')
if not os.path.isfile(_clojure_path):
    raise RuntimeError("required: %s" % _clojure_path)


class Clojure(TestScript):
    bin = "java -cp %s:. clojure.main" % _clojure_path
    temp_filename = "tmp.clj"
    human_name = "Clojure"
    pygments_name = "clojure"
    embedded_output_pattern = (
        r"\(comment \(output checked by coderunner\)"
        r"(.*)"
        r"\(end of comment\)\)")


class _Scheme(TestScript):
    temp_filename = "tmp.scm"
    pygments_name = "scheme"


class Gauche(_Scheme):
    bin = "gosh"
    human_name = "Gauche"


class Scheme(Gauche):
    human_name = "Scheme"


class Java(Test):
    human_name = "Java"
    temp_filename = "Tmp.java"
    pygments_name = "java"
    bin = "javac"

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


class Java7(Java):
    human_name = "Java7"
    pygments_name = "java7"
    bin = "javac7"


class LangC(Test):
    human_name = "C"
    temp_filename = "tmp.c"
    embedded_output_pattern = r"/\* output \(checked by coderunner\)(.*) \*/"
    pygments_name = "c"
    bin = "gcc"

    def run(self):
        if not self.is_file:
            file(self.filename, "w").write(self.code)

        cmd = ("gcc").split() + [self.filename]
        ret = self.subproc(cmd)
        if self.to_run:
            ret += self.subproc(["env", "./a.out"])
        self.check_expect(ret)

class Cpp(Test):
    human_name = "C++"
    temp_filename = "tmp.cpp"
    embedded_output_pattern = _multi_pattern(
        r"/\* output \(checked by coderunner\)(.*) \*/",
        r"//-> ([^\n]+)\n")
    pygments_name = "cpp"
    bin = "g++"

    def __init__(self, code, expect="", extra_option=[], **kw):
        self.extra_option = extra_option
        super(Cpp, self).__init__(code, expect, **kw)

    def run(self):
        if not self.is_file:
            file(self.filename, "w").write(self.code)

        cmd = (
            ("env LC_ALL=en g++ -Wall -W -Wformat=2 -Wcast-qual -Wcast-align "
             "-Wwrite-strings -Wconversion -Wfloat-equal "
             "-Wpointer-arith -Woverloaded-virtual -Wnon-virtual-dtor "
             "-I/opt/local/include/ -O3").split()
            + self.extra_option + [self.filename])
        ret = self.subproc(cmd)
        if self.to_run:
            #TODO: (assert not ret) should be test failure
            ret = self.subproc(["env", "./a.out"])
        self.check_expect(ret)


class CSharp(Test):
    human_name = "C#"
    temp_filename = "tmp.cs"
    embedded_output_pattern = _multi_pattern(
        r"/\* output \(checked by coderunner\)(.*) \*/",
        r"//-> ([^\n]+)\n")
    pygments_name = "cs"
    bin = "gmcs"

    def __init__(self, code, expect="", extra_option=[], **kw):
        self.extra_option = extra_option
        super(CSharp, self).__init__(code, expect, **kw)

    def run(self):
        if not self.is_file:
            file(self.filename, "w").write(self.code)

        cmd = ["gmcs", self.filename]
        ret = self.subproc(cmd)
        if self.to_run:
            #TODO: (assert not ret) should be test failure
            ret = self.subproc(["mono", "tmp.exe"])
        self.check_expect(ret)


def test(lang, *args, **kw):
    "register tests"
    tests.append(
        lang(*args, **kw))

def drop_tests():
    """delete already registered tests.
    It is useful when you are writing a lot of tests"""
    global tests
    tests = []

def main():
    global args
    parser = argparse.ArgumentParser(description='run codes and check output')
    parser.add_argument(
        '--format', dest='format', action='store',
        help=(
            "Print codes and expected outputs in specified format. "
            "When it is specified, not run codes. "
            "(supported: rest, mybook)"))
    parser.add_argument(
        '--lang-format', dest='lang_format', action='store', default="heading",
        help=(
            "Print language's name (such as 'Python') in specified format. "
            "(supported: heading(default), strong, none)"))
    parser.add_argument(
        '--suppress-expected', dest='suppress_expected', action='store_true',
        help=(
            "For --format=rest. Don't show expected output."))
    parser.add_argument(
        '--nonstop', dest='nonstop', action='store_true',
        help=(
            "Don't stop on failure and run all tests."))
    parser.add_argument(
        '--copy', dest='copy_got_output', action='store_true',
        help=(
            "Copy got output into clipboard. (Mac only)"))

    args = parser.parse_args()
    if not args.format:
        for test in tests:
            test.run()
        print "ok."
    else:
        for test in tests:
            test.show()


def _test():
    import doctest
    doctest.testmod()

def _test_executables():
    print "check whether expected executables exist:"
    for lang in [Python, Ruby, Perl, JS, Scheme, Java, LangC, Cpp]:
        cmd = "which %s" % lang.bin
        ret = subprocess.call(cmd, shell=True, env={"PATH": PATH})
        if ret != 0:
            print (
                "Test '%s' expected executable named '%s' in $PATH. " % (
                lang.__name__, lang.bin))
            print "  install it or make symbolic link to it in coderunner/bin/"


if __name__ == "__main__":
    _test()
    _test_executables()
