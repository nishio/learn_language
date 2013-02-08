import subprocess
import os
import shutil
import collect_readme

toc = []

def process(testfile, title, outputfile, option=[]):
    print "processing %s(%s)" % (title, testfile)
    testdir, testscript = os.path.split(testfile)

    if testdir:
        CWD = os.getcwd()
        os.chdir(testdir)

    ret = subprocess.check_output([
            "python", testscript, "--format=rest"] + option)

    if testdir:
        os.chdir(CWD)

    fo = file(os.path.join("source", outputfile) , "w")
    fo.write("=" * len(title))
    fo.write("\n%s\n" % title)
    fo.write("=" * len(title))
    fo.write("\n\n")
    fo.write(ret)
    toc.append(outputfile)
    print title, "done"


def generate_index():
    INDEX = "source/test_index.rst"
    shutil.copy("rst_template/test_index.rst", INDEX)
    collect_readme.update_toc(toc, target=INDEX, maxdepth=1)


process(
    "../coderunner/test/hello.py",
    "hello", "hello.rst",
    option=["--suppress-expected"])

process(
    "../coderunner/test/zero_division.py",
    "1 / 0", "zero_division.rst")

process(
    "../coderunner/test/division.py",
    "1 / 2", "division.rst")

process(
    "../with-block/test.py",
    "With-statement", "with_statement.rst")

process(
    "../python/errors.py",
    "Python Errors", "python_errors.rst",
    option=["--lang-format=none"])


process(
    "../python/2and3.py",
    "Python 2 and 3", "python_2and3.rst",
    option=["--lang-format=strong"])

generate_index()
