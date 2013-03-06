"""
output in ReST format
"""

def _indent(s):
    r"""
    >>> _indent("aaa")
    '  aaa'
    >>> _indent("aaa\nbbb")
    '  aaa\n  bbb'
    """
    return "\n".join("  " + line for line in s.split("\n"))


def print_contents():
    print '.. contents::\n   :local:\n'


def show_header(format, name):
    print '\n'
    if format == "strong":
        print "**%s**" % name
    elif format == "none":
        pass # print nothing
    else: # default: "heading"
        print name
        print "-" * max(len(name), 5)


def show_pre(code, pygments=None):
    if pygments:
        print
        print ".. code-block:: %s" % pygments
        print
    else:
        print
        print "::"
        print
    print _indent(code)
    print
