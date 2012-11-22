====================
 learn_language/doc
====================

This is a tool to make html files on
http://nhiro.org/learn_language/
from test codes and README of other repository.

make_source.py generates \*.rst,
and Sphinx builds them into html files.

http://nhiro.org/learn_language/index.html comes from learn_language/README.rst.

Usage::

  $ make source
  $ make html

Usage(for me)::

  $ make deploy # it copies files for my entrypoint project.

  I need "$ make deploy" on entrypoint project to send files on server.

TODO
====

- use 'git submodule' to store other repository in ./repos/ (now it was cloned)


