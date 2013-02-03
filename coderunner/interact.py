r"""
communicate with interactive subprocess, such as GHCi, and get its output

>>> s = interact('ghci', ':t 1\n')
>>> get_ghci_body(s)
'Prelude> :t 1\r\r\n1 :: (Num t) => t'

>>> s = interact('swipl', 'X = 1 - 1.\n')
>>> get_swipl_body(s)
'?- X = 1 - 1.\r\nX = 1-1.'

>>> s = interact('python', 'import this\n')
>>> get_python_body(s).split('\r\n')[:2]
['>>> import this', 'The Zen of Python, by Tim Peters']

"""

import subprocess
from select import select
import os
import tty
import pty
import re

ESCAPE_SEQUENCE = '\x1B\[...|\x1b[^[]'

# ported from 'pty' library
STDIN_FILENO = 0

CHILD = 0

def spawn(argv, master_read, stdin_read, commands_to_run):
    """Create a spawned process."""
    if type(argv) == type(''):
        argv = (argv,)
    pid, master_fd = pty.fork()
    if pid == CHILD:
        os.execlp(argv[0], *argv)
    try:
        mode = tty.tcgetattr(STDIN_FILENO)
        tty.setraw(STDIN_FILENO)
        restore = 1
    except tty.error:    # This is the same as termios.error
        restore = 0
    try:
        pty._writen(master_fd, commands_to_run)
        _copy(master_fd, master_read, stdin_read)
    finally:
        if restore:
            tty.tcsetattr(STDIN_FILENO, tty.TCSAFLUSH, mode)
    os.close(master_fd)


def _copy(master_fd, master_read, stdin_read):
    fds = [master_fd]
    while True:
        rfds, wfds, xfds = select(fds, [], [], 1.0)
        if not rfds: break
        data = master_read(master_fd)
        if not data:  # Reached EOF.
            break


def interact(shell, commands_to_run):
    typescript = open('typescript', 'w')

    def read(fd):
        data = os.read(fd, 1024)
        typescript.write(data)
        return data

    def read2(fd):
        data = os.read(fd, 1024)
        return data

    spawn(shell, read, read2, commands_to_run)
    typescript.close()

    data = open('typescript').read()
    data = remove_escape_sequence(data)
    return data

def remove_escape_sequence(s):
    return re.sub(ESCAPE_SEQUENCE, '', s)


def get_ghci_body(s):
    m = re.search(r'Prelude>.*(?=\r\n\w+>)', s, re.DOTALL)
    return m.group()


def get_swipl_body(s):
    m = re.search(r'\r\n\r\n(\?- .*)(?=\r\n\r\n\?- )', s, re.DOTALL)
    return m.groups()[0]


def get_python_body(s):
    m = re.search(r'>>>.*(?=\r\n>>>)', s, re.DOTALL)
    return m.group()


def _test():
    import doctest
    doctest.testmod()


if __name__ == '__main__':
    _test()
