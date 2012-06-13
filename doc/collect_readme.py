"""
collect readme

copy such as:
coderunner/README.rst -> source/coderunner.rst
../README.rst -> index.rst
"""
import os
import shutil

def copy_readme(src, dst=None):
    if not dst:
        dst = os.path.split(src)[1]
    toc.append(dst)
    if os.path.isdir(src):
        src = os.path.join(src, "README.rst")

    shutil.copy(src, "source/%s.rst" % dst)

def make_toc(xs):
    buf = [".. toctree::"]
    for x in xs:
        buf.append("   %s" % x)
    return "\n".join(buf)

def update_toc():
    data = file(INDEX).read()
    data = data.replace(
        ".. toctree::", make_toc(toc))
    file(INDEX, "w").write(data)


INDEX = "source/index.rst"
# copy index
shutil.copy("../README.rst", INDEX)
toc = []
copy_readme("../coderunner")
copy_readme("../doc")
update_toc()
