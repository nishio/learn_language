"""
Classes to write document
"""
import coderunner

class _Base(object):
    def show(self):
        if coderunner.args.format == "rest":
            self.show_in_rest()
        else:
            raise NotImplementedError, args.format

    def run(self):
        pass

class Comment(_Base):
    """
    Object to write comment
    """
    def __init__(self, content):
        self.content = content

    def show_in_rest(self):
        print
        print self.content
        print


class Header(_Base):
    """
    Object to write comment
    """
    def __init__(self, content, level=0):
        """
        level: 0, 1, 2
        """
        self.content = content
        self.level = level

    def show_in_rest(self):
        line = "=-~"[self.level]
        print
        print self.content
        print line * len(self.content)
        print


def header(content, level=0):
    coderunner.tests.append(Header(content, level))


def comment(content):
    coderunner.tests.append(Comment(content))
