import os, pty
import subprocess

fo = file('tmp.hs', 'w')
fo.write('xs = %s' % range(10))
fo.close()

shell = 'ghci'
typescript = open('typescript', 'w')
commands_to_run = """\
:load tmp.hs
seq xs ()
:print xs
\x04
"""

import time
def read(fd):
    data = os.read(fd, 1024)
    typescript.write(data)
    return data

def read2(fd):
    data = os.read(fd, 1024)
    return data

"""
from pty
"""
from select import select
import os
import tty

STDIN_FILENO = 0

CHILD = 0

def spawn(argv, master_read, stdin_read):
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


spawn(shell, read, read2)


typescript.close()
# show
import re
ESCAPE_SEQUENCE = '\x1B\[...|\x1b[^[]'
data = open('typescript').read()
data = re.sub(ESCAPE_SEQUENCE, '', data)
data = re.search(r'Prelude>.*(?=[*]\w+> [\s]+Leaving GHCi.)', data, re.DOTALL)
print data.group()
