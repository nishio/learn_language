====================
 learn_language/doc
====================

This is a tool to make html files on
http://nhiro.org/learn_language/
from test codes and README of other repository.

make_source.py generates \*.rst,
and Sphinx builds them into html files.

Usage::

  $ make source
  $ make html
  $ make deploy # it need permission to my server


TODO
====

- use 'git submodule' to store other repository in ./repos/ (now it was cloned)


