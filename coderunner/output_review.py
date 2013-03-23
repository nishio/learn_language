"""
output in ReVIEW format
"""

def _indent(s):
    r"""
    >>> _indent("aaa")
    '  aaa'
    >>> _indent("aaa\nbbb")
    '  aaa\n  bbb'
    """
    return "\n".join("  " + line for line in s.split("\n"))

def show_code(code, _notused):
    print '//emlistnum{'
    print _indent(code)
    print '//}'

def show_output(s):
    print '//cmd{'
    print _indent(s)
    print '//}'
