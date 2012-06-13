====================
 learn_language/doc
====================

This is a tool to make html files on
http://nishio.github.com/learn_language/
from test codes.

make_source.py generates *.rst,
and Sphinx builds them into html files.

Usage::

  $ make source
  $ make html
  $ make deploy # need write access to the repository


To 'make deploy' we need to checkout the learn_language repository's gh-pages branch as name 'gh-pages'.
