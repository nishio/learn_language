============
 coderunner
============

This is a tool to run codes and check outputs.

When you learn/teach programming languages
you will write small codes.

Pairs of those codes and outputs are *tests*.
To store and run them helps to know what is changed.

Usage
=====

::

  $ python coderunner.py # run self tests
  $ python test/hello.py # run 'print hello' tests


Expected executables
====================

Self test warns if expected executables don't found::

   coderunner$ python coderunner.py
   check whether expected executables exist:
   /home/rackhuber/.pythonbrew/pythons/Python-2.7.3/bin/python2.7
   Test 'Ruby' expected executable named 'ruby1.9' in $PATH.
     install it or make symbolic link to it in coderunner/bin/
   Test 'Perl' expected executable named 'perl5' in $PATH.
     install it or make symbolic link to it in coderunner/bin/
   /usr/bin/rhino
   Test 'Scheme' expected executable named 'gosh' in $PATH.
     install it or make symbolic link to it in coderunner/bin/
   /usr/bin/javac
   /usr/bin/gcc
   /usr/bin/g++

It can fix as follow::

   coderunner/bin$ ln -s /home/rackhuber/.rvm/rubies/ruby-1.9.2-p320/bin/ruby ruby1.9
   coderunner/bin$ ln -s /usr/bin/perl5.14.2 perl5
   coderunner/bin$ sudo apt-get install gauche


TODO
====

- To make output better, add heading between test? Add description to tests?
  http://nishio.github.com/learn_language/test_index.html