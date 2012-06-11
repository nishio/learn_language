import subprocess

pages = []

def process(testfile, title, outputfile, option=[]):
    ret = subprocess.check_output([
            "python", testfile, "--format=rest"] + option)
    fo = file(outputfile, "w")
    fo.write("=" * len(title))
    fo.write("\n%s\n" % title)
    fo.write("=" * len(title))
    fo.write("\n\n")
    fo.write(ret)
    pages.append(outputfile)
    print title, "done"


def generate_index():
    fo = file("index.rst", "w")
    fo.write("""
Welcome to Learn Language's documentation!
==========================================

This project is currently storing small test codes and its output.

.. raw:: html

   For detail, visit my repository:
   <a href="https://github.com/nishio/learn_language/"
      onclick="pageTracker._trackPageview('/github')">
      https://github.com/nishio/learn_language/
   </a>

Contents:

.. toctree::
   :maxdepth: 1

""")
    for page in pages:
        fo.write("   %s\n" % page)

    fo.close()


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
    "../python/errors.py",
    "Python Errors", "python_errors.rst")

generate_index()
