import os, pty
import subprocess

fo = file('tmp.hs', 'w')
fo.write('xs = %s' % range(10))
fo.close()

shell = 'ghci'
typescript = open('typescript', 'w')
input_buffer = """\
:load tmp.hs
seq xs ()
:print xs
\x04
"""

import time
def read(fd):
    #typescript.write('<r:%s>' % time.time())
    data = os.read(fd, 1024)
    typescript.write(data)
    return data

def read2(fd):
    data = os.read(fd, 1024)
    #typescript.write('<r2:%s:%r>' % (time.time(), data))
    return data

"""
from pty
"""
from select import select
import os
import tty

STDIN_FILENO = 0
STDOUT_FILENO = 1
STDERR_FILENO = 2

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
        pty._writen(master_fd, input_buffer)
        _copy(master_fd, master_read, stdin_read)
    finally:
        if restore:
            tty.tcsetattr(STDIN_FILENO, tty.TCSAFLUSH, mode)
    os.close(master_fd)

def _copy(master_fd, master_read, stdin_read):
    """Parent copy loop.
    Copies
            pty master -> standard output   (master_read)
            standard input -> pty master    (stdin_read)"""
    fds = [master_fd]
    while True:
        rfds, wfds, xfds = select(fds, [], [], 1.0)
        if not rfds: break
        if master_fd in rfds:
            data = master_read(master_fd)
            if not data:  # Reached EOF.
                fds.remove(master_fd)
            else:
                os.write(STDOUT_FILENO, data)


spawn(shell, read, read2)



