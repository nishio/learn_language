r"""
communicate with interactive subprocess, such as GHCi, and get its output

>>> s = interact('ghci', ':t 1\n' + EOT)
>>> get_ghci_body(s)
'Prelude> :t 1\n1 :: (Num t) => t'

>>> s = interact('swipl', 'X = 1 - 1.\n' + EOT)
>>> get_swipl_body(s)
'?- X = 1 - 1.\nX = 1-1.'

>>> s = interact('python', 'import this\n' + EOT)
>>> get_python_body(s).split('\n')[:2]
['>>> import this', 'The Zen of Python, by Tim Peters']

Scala takes more than 1 second (default timeout) to respond.
I set timeout=10.0 to wait it.

>>> s = interact('scala-2.10', '1\n' + EOT, timeout=10.0)
>>> get_scala_body(s)
'scala> 1\nres0: Int = 1'
"""

from select import select
import os
import pty
import re

EOT = '\x04'  # ^D: End of Transmission
ESCAPE_SEQUENCE = (
    '\x1B\[\d+(;\d+)*m|'  # color
    '\x1B\[\d+;\d+[Hf]|'  # move cursor absolute
    '\x1B\[\d*[ABCD]|'    # move cursor relative
    '\x1B\[[DMELsu]|'     # other cursor?
    '\x1B\[\?1[lh]|'      # ? from GHCi
    '\x1B[=>]|'           # ? from GHCi
    '\x1B\[0?J|'          # delete back
    '\x1B\[1J|'           # delete forward?
    '\x1B\[2J|\x1B\*|'    # clear screen
    '\x1B\[0?K|'          # kill right line
    '\x1B\[1K|'           # kill left line
    '\x1B\[2K|'           # kill whole line
    '\x1B\[6n')           # console input?

# ported from 'pty' library
STDIN_FILENO = 0

CHILD = 0

def spawn(argv, master_read, stdin_read, commands_to_run, timeout):
    """Create a spawned process."""
    if type(argv) == type(''):
        argv = (argv,)
    pid, master_fd = pty.fork()
    if pid == CHILD:
        os.execlp(argv[0], *argv)

    pty._writen(master_fd, commands_to_run)

    fds = [master_fd]
    while True:
        rfds, wfds, xfds = select(fds, [], [], timeout)
        if not rfds:  # timeout
            break
        data = master_read(master_fd)
        if not data:  # Reached EOF.
            break

    os.close(master_fd)
# end: ported from 'pty' library

def interact(shell, commands_to_run, timeout=1.0):
    typescript = open('tmp.log', 'w')

    def read(fd):
        data = os.read(fd, 1024)
        typescript.write(data)
        typescript.flush()
        return data

    def read2(fd):
        data = os.read(fd, 1024)
        return data

    spawn(shell, read, read2, commands_to_run, timeout)
    typescript.close()

    data = open('typescript').read()
    return remove_escape_sequence(data)

def remove_escape_sequence(s):
    return re.sub(ESCAPE_SEQUENCE, '', s)


def get_ghci_body(s):
    m = re.search(r'Prelude>.*(?=\r\n\w+>)', s, re.DOTALL)
    ret = m.group()
    # nomarlize newline
    ret = ret.replace('\r\n', '\n')
    ret = ret.replace('\r', '')
    return ret


def get_swipl_body(s):
    m = re.search(r'\r\n\r\n(\?- .*)(?=\r\n\r\n\?- )', s, re.DOTALL)
    ret = m.groups()[0]
    # nomarlize newline
    ret = ret.replace('\r\n', '\n')
    ret = ret.replace('\r', '')
    return ret


def get_python_body(s):
    m = re.search(r'>>>.*(?=\r\n>>>)', s, re.DOTALL)
    ret = m.group()
    ret = ret.replace('\r\n', '\n')
    return ret


def get_scala_body(s):
    m = re.search(r'scala>.*(?=\r\n\r\nscala>)', s, re.DOTALL)
    ret = m.group()
    ret = ret.replace('\r\n', '\n')
    return ret


def _test():
    import doctest
    doctest.testmod()


if __name__ == '__main__':
    _test()
