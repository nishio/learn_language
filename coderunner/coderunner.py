# -*- coding: utf-8 -*-
'''
code runner: tools to run small codes (sample code of documents)

USAGE: register tests with 'test' func, then call 'main'
see doc of 'test' for its arguments

test(Python,
"""
1/0
""", """
Traceback (most recent call last):
  File "tmp.py", line 1, in <module>
    1/0
ZeroDivisionError: integer division or modulo by zero
""")

test(Java, "exception.java", is_file=True, to_run=False)
'''
import argparse
import subprocess
import difflib
import os
import sys
import re
import interact
from docwriter import header, comment
import langspec

tests = []
BIN_PATH = os.path.join(os.path.abspath(
        os.path.dirname(__file__)), 'bin')
PATH = ":".join([BIN_PATH] + os.environ.get('PATH', '').split(":"))

EMBEDDED_OUTPUT_PATTERN_LIKE_C = r"/\* output \(checked by coderunner\)(.*[^ ]) ?\*/"

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
    if prefix:
        pre = "(?<=%s)" % prefix  # positive lookbehind assertion
    else:
        pre = ''
    if suffix:
        suf = "(?=%s)" % suffix  # lookahead assertion
    else:
        suf = ''
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


class CantRunSubprocess(RuntimeError): pass

def _subproc(cmd):
    """
    call subprocess `cmd` and get its output
    >>> _subproc(['echo', 'foo'])
    'foo'
    """
    try:
        p = subprocess.Popen(
            cmd,
            stderr=subprocess.STDOUT,
            stdout=subprocess.PIPE,
            env={"PATH": PATH})
        ret, _dummy = p.communicate("")
        return ret

    except OSError, e:
        assert str(e) == '[Errno 2] No such file or directory'
        raise CantRunSubprocess("Can't run subprocess", cmd)


class Test(object):
    """
    Basic test runner

    embedded_output_pattern:
      regular expression to find output desctiption

    dontcare_pattern:
      regular expression to ignore part of output
    """
    embedded_output_pattern = None
    dontcare_pattern = None
    pygments_name = 'none'

    def check_expect(self, ret):
        """
        check whether ret == self.expect and show if not.
        """
        # replace `don't care pattern` (not to care difference)
        if self.dontcare_pattern:
            self.expect = re.sub(
                self.dontcare_pattern,
                "..dontcare..", self.expect, re.DOTALL)
            ret = re.sub(
                self.dontcare_pattern,
                "..dontcare..", ret, re.DOTALL)

        ret = ret.strip("\n")
        if ret != self.expect:
            print
            print "ERROR"
            if self.is_file:
                print "file:", self.filename
            else:
                print "code " + "=" * 35
                print self._code_as_utf8()
                print "=" * 40

            expectlines = self.expect.split("\n")
            gotlines = ret.split("\n")
            difflines = list(difflib.unified_diff(
                    expectlines, gotlines, "expected", "got"))
            if args.use_diff and len(difflines) < len(expectlines) + len(gotlines):
                print "diff " + "=" * 35
                print self._as_utf8("\n".join(difflines))
                print "=" * 40
            else:
                print "expected " + "=" * 31
                print self._expect_as_utf8()
                print "got " + "=" * 36
                print self._as_utf8(ret)
                print "=" * 40
            if not args.nonstop:
                if args.copy_got_output:
                    # copy result to clipboard (now Mac only)
                    p = subprocess.Popen(["pbcopy"], stdin=subprocess.PIPE)
                    p.stdin.write(ret)
                    p.stdin.close()
                sys.exit(1)

    def show(self):
        if args.format == "rest":
            self.show_in_rest()
        else:
            raise NotImplementedError, args.format

    def _show_header_in_rest(self):
        if args.lang_format == "strong":
            print "**%s**" % self.human_name
        elif args.lang_format == "none":
            pass # print nothing
        else: # default: "heading"
            print self.human_name
            print "=" * len(self.human_name)

    def show_in_rest(self):
        """
        show code. currently output ReST (for my book)
        """
        self._show_header_in_rest()
        print
        print ".. code-block:: %s" % self.pygments_name
        print
        print _indent(self._code_as_utf8().strip("\n"))
        if not args.suppress_expected:
            expected = self._expect_as_utf8().strip("\n")
            if expected == "": expected = "(no output)"
            print
            print "::"
            print
            print _indent(expected)
        print "\n"

    def _code_as_utf8(self):
        if self.source_encoding:
            return self.code.decode(self.source_encoding).encode('utf-8')
        return self.code

    def _expect_as_utf8(self):
        return self._as_utf8(self.expect)

    def _as_utf8(self, output):
        if self.output_encoding:
            return output.decode(self.output_encoding).encode('utf-8')
        return output

    def __init__(self, code, expect="", is_file=False,
                 to_run=True, is_embedded_output=False,
                 extra_dontcare=None, source_encoding=None,
                 output_encoding=None):
        """
        is_file: when code is large you can put it in the other file
        to_run: False when you don't want to run
                (especially in Java, C++, you may want to check
                 the code fail to compile)
        is_embedded_output: whether output is embedded in the given code
        source_encoding: if be set, convert from given encoding to UTF-8 (default None)
        output_encoding: if be set, convert from given encoding to UTF-8 (default None)
        """
        self.source_encoding = source_encoding
        self.output_encoding = output_encoding
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

        if extra_dontcare != None:
            if self.dontcare_pattern:
                self.dontcare_pattern += '|' + extra_dontcare
            else:
                self.dontcare_pattern = extra_dontcare

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


    version_option = ["-v"]
    @classmethod
    def get_version(cls):
        cmd = [cls.bin] + cls.version_option
        ret = _subproc(cmd)
        lines = ret.split('\n')
        if len(lines) > 3:
            filtered = [line for line in lines if 'version' in line]
            if filtered:
                return "".join(filtered)
            import pdb
            pdb.set_trace()
        return ret


class TestScript(Test):
    def run(self):
        if not self.is_file:
            file(self.filename, "w").write(self.code)

        ret = _subproc(self.bin.split() + [self.filename])
        self.check_expect(ret)

        if not self.is_file:
            os.remove(self.filename)


class _Python(TestScript):
    pygments_name = "python"
    temp_filename = "tmp.py"
    dontcare_pattern = _pattern(r" at ", "0x[0-9a-fX]+", r">")
    embedded_output_pattern = r'"""output \(checked by coderunner\)(.*)"""'
    version_option = ["-V"]


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
    dontcare_pattern = _multi_pattern(
        # 3 lines before error
        r"(\n[^\n]*){3}\n(?=\w*Error: )",
        # detail stacktrace
        r"(    at[^\n]+\n?)+")


class Rhino(_JS):
    bin = "rhino"
    human_name = "Rhino"


class JS(NodeJS):
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
    version_option = ['-V']
    human_name = "Gauche"


class Scheme(Gauche):
    human_name = "Scheme"


class CommonLisp(TestScript):
    human_name = "Common Lisp"
    bin = "clisp"
    temp_filename = "tmp.lisp"
    version_option = ['--version']


class Haskell(TestScript):
    human_name = "Haskell"
    bin = "runghc"
    temp_filename = "tmp.hs"
    pygments_name = "haskell"


class _Smalltalk(TestScript):
    temp_filename = "tmp.st"
    pygments_name = "smalltalk"


class Squeak(_Smalltalk):
    human_name = "Squeak"
    bin = "run_squeak.py"  # in 'bin' dir

    def __init__(self, code, expect="", is_error=False, **kw):
        if is_error:
            code = (langspec.squeak.PREFIX_CODE_CATCH_ERROR
                    + code +
                    langspec.squeak.SUFFIX_CODE_CATCH_ERROR)
        else:
            code = (langspec.squeak.PREFIX_CODE
                    + code +
                    langspec.squeak.SUFFIX_CODE)

        super(_Smalltalk, self).__init__(code, expect, **kw)


class GNUSmalktalk(_Smalltalk):
    human_name = "GNU Smalltalk"
    bin = "gst"


class Smalltalk(GNUSmalktalk):
    human_name = "Smalltalk"


class Scala(TestScript):
    temp_filename = "tmp.scala"
    human_name = "Scala"
    pygments_name = "scala"
    bin = "scala-2.10"
    # don't care fullpath on error message
    dontcare_pattern = _multi_pattern(
        _pattern('^', '.*', 'tmp\.scala:'),
        r'\.\.\.')

class TestTwoPhase(Test):
    """
    Test runner for two phased (compile and run) language
    """
    def __init__(self, code, expect="", extra_option=[],
                 ignore_warning=False, **kw):
        """
        ignore_warning: ignore compile warnings (default: False)
        """
        self.extra_option = extra_option
        self.ignore_warning = ignore_warning
        super(TestTwoPhase, self).__init__(code, expect, **kw)

    def run(self):
        if not self.is_file:
            file(self.filename, "w").write(self.code)

        ret = self.compile_phase()

        if self.to_run:
            if self.ignore_warning: ret = ""
            if ret != "":
                raise AssertionError(
                    "You try to run but compiler show following message:\n"
                    + ret + "\nYou can use option ignore_warning=True to ignore, or to_run=False to abort")
            ret += self.run_phase()
        self.check_expect(ret)

        if not self.is_file:
            os.remove(self.filename)

    def compile_phase(self):
        cmd = (self.bin.split() + self.extra_option + [self.filename])
        ret = _subproc(cmd)
        return ret

    def run_phase(self):
        ret = _subproc(self.runtime.split())
        return ret


class Java(TestTwoPhase):
    human_name = "Java"
    temp_filename = "Tmp.java"
    embedded_output_pattern = EMBEDDED_OUTPUT_PATTERN_LIKE_C
    pygments_name = "java"
    bin = "env LC_ALL=en javac -J-Duser.language=en"
    runtime = "env LC_ALL=en java -Duser.language=en -cp ."
    version_option = ['-version']

    def run_phase(self):
        trunk = self.filename.replace(".java", "")
        ret = _subproc(self.runtime.split() + [trunk])
        return ret


class Java7(Java):
    human_name = "Java7"
    pygments_name = "java"
    bin = "javac7"
    runtime = "java7"


class LangC(TestTwoPhase):
    human_name = "C"
    temp_filename = "tmp.c"
    embedded_output_pattern = EMBEDDED_OUTPUT_PATTERN_LIKE_C
    pygments_name = "c"
    bin = "gcc"
    runtime = "env ./a.out"

class Cpp(TestTwoPhase):
    human_name = "C++"
    temp_filename = "tmp.cpp"
    embedded_output_pattern = _multi_pattern(
        EMBEDDED_OUTPUT_PATTERN_LIKE_C,
        r"//-> ([^\n]+)\n")
    pygments_name = "cpp"
    bin = ("env LC_ALL=en g++ -Wall -W -Wformat=2 -Wcast-qual -Wcast-align "
           "-Wwrite-strings -Wconversion -Wfloat-equal "
           "-Wpointer-arith -Woverloaded-virtual -Wnon-virtual-dtor "
           "-I/opt/local/include/ -O3")
    runtime = "env ./a.out"


class CSharp(TestTwoPhase):
    human_name = "C#"
    temp_filename = "tmp.cs"
    embedded_output_pattern = _multi_pattern(
        EMBEDDED_OUTPUT_PATTERN_LIKE_C,
        r"//-> ([^\n]+)\n")
    pygments_name = "csharp"
    bin = "gmcs"
    version_option = ['--version']
    runtime = "mono"

    def run_phase(self):
        exename = self.filename.replace(".cs", ".exe")
        ret = _subproc(["mono", exename])
        return ret


class TestInteractive(Test):
    default_timeout = 1.0
    def __init__(self, code, expect="", timeout=None, **kw):
        if timeout == None: timeout = self.default_timeout
        self.timeout = timeout
        if not code.endswith('\n'):
            code += '\n'
        code += interact.EOT
        super(TestInteractive, self).__init__(code, expect, **kw)

    def run(self):
        ret = interact.interact(
            self.bin.split(),
            self.code, self.timeout)

        ret = self.get_result(ret)
        self.check_expect(ret)

    def get_result(self, s):
        raise NotImplementedError

    def show_in_rest(self):
        """
        in Interactive test, self.code is repeated in self.expect,
        so no need to print it.
        """
        self._show_header_in_rest()
        expected = self._expect_as_utf8().strip("\n")
        if expected == "": raise AssertionError('%s has no expected output')
        print
        print "::"
        print
        print _indent(expected)
        print "\n"


class GHCi(TestInteractive):
    human_name = "Haskell"
    temp_filename = "tmp.hs"
    pygments_name = "haskell"
    bin = "ghci"

    def get_result(self, s):
        return interact.get_ghci_body(s)


class Prolog(TestInteractive):
    human_name = "Prolog"
    temp_filename = "tmp.pl"
    pygments_name = "prolog"
    bin = "swipl"  # SWI-Prolog

    def __init__(self, code, expect="", timeout=None, **kw):
        self.modules = []
        super(Prolog, self).__init__(code, expect, **kw)

    def get_result(self, s):
        return interact.get_swipl_body(s)

    def with_module(self, name, code):
        file('%s.pl' % name, 'w').write(code)
        self.modules.append(name)

    def run(self):
        code = self.code
        for name in self.modules:
            code = "[%s].\n" % name + code  # load modules

        ret = interact.interact(
            self.bin.split(),
            code, self.timeout)

        ret = self.get_result(ret)
        self.check_expect(ret)
        for name in self.modules:
            os.remove("%s.pl" % name)


class ScalaInteractive(TestInteractive):
    human_name = "Scala"
    temp_filename = "tmp.scala"
    pygments_name = "scala"
    bin = "scala-2.10"  # SWI-Prolog
    default_timeout = 10.0

    def get_result(self, s):
        return interact.get_scala_body(s)


def test(lang, code, expect='', *args, **kw):
    """register tests
    lang: instance of Test class,
          which holds how to test given code
          especially which language it is

    code: code to test.

    expect: expected output of given code
            optional (default: '')

    optional arguments(foo=bar means bar is default value)

    if_file=False: When True, ``code`` is a path to another file.

    to_run=True: When False, ``code`` will not be run.
                 It is used expecially in Java, C++,
                 when you want to check behavoir on compile phase

    is_embedded_output=False:
        When True, expected output is embedded in the given code
        (usually with in_file=True)
        see ``embedded_output_pattern`` to know how to embed them.

    """
    t = lang(code, expect, *args, **kw)
    tests.append(t)
    return t


def drop_tests():
    """delete already registered tests.
    It is useful when you are writing a lot of tests"""
    global tests
    tests = []


def run_a_test(lang, code, expect='', *xs, **kw):
    """
    Run a test without calling ``main``.
    It is for doctest of myself.

    >>> run_a_test(Python, 'print 1+1', '2')
    """
    args.nonstop = True  # don't call sys.exit on fail
    args.copy_got_output = False
    t = lang(code, expect, *xs, **kw)
    t.run()


def main():
    global args
    parser = argparse.ArgumentParser(description='Run codes and check outputs are as expected.')

    parser.add_argument(
        '--format', dest='format', action='store',
        help=(
            "Print codes and expected outputs in specified format. "
            "When it is specified, not run codes. "
            "(supported: rest)"))
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
    parser.add_argument(
        '--no-diff', dest='use_diff', action='store_false',
        help=(
            "show diff of expected and got outputs (default: True)"))

    args = parser.parse_args()

    if not args.format:
        print "%d tests..." % len(tests)
        for test in tests:
            try:
                test.run()
            except CantRunSubprocess, e:
                print "can't run subprocess '%s', ignored" % " ".join(e.args[1])
        print "ok."
    else:
        for test in tests:
            test.show()


def _test():
    import doctest
    doctest.testmod()


def _test_executables():
    print "check whether expected executables exist:"
    for lang in [Python, Ruby, Perl, JS, Scheme, Java, LangC, Cpp, CSharp]:
        print lang.human_name
        cmd = "which %s" % lang.bin
        ret = subprocess.call(cmd, shell=True, env={"PATH": PATH})
        if ret != 0:
            print (
                "Test '%s' expected executable named '%s' in $PATH. " % (
                lang.__name__, lang.bin))
            print "  install it or make symbolic link to it in coderunner/bin/"


def print_version():
    for lang in [Python, Ruby, Perl, JS, Scheme, Java, LangC, Cpp, CSharp]:
        print lang.human_name
        print lang.get_version()

def _main():
    """main function when coderunner.py was called as a script (not imported as library)"""
    global args
    parser = argparse.ArgumentParser(description='Run codes and check outputs are as expected.')
    parser.add_argument('--self-test', action='store_true',
                        help='run coderunner\'s doctest')
    parser.add_argument('--exec-test', action='store_true',
                        help='test executables availability')
    parser.add_argument('--print-versions', action='store_true',
                        help='print versions of executables')

    args = parser.parse_args()

    if args.self_test:
        _test()
    elif args.exec_test:
        _test_executables()
    elif args.print_versions:
        print_version()
    else:
        print 'running self-test'
        _test()
        print 'ok.'

if __name__ == "__main__":
    _main()
