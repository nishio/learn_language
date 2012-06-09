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
Welcome to LearnLanguage's documentation!
=========================================

Contents:

.. toctree::
   :maxdepth: 2

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

generate_index()
