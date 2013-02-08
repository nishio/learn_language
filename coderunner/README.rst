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

  $ python coderunner.py              # run self tests
  $ python coderunner.py --exec-test  # run executable tests
  $ python test/hello.py              # run 'print hello' tests

It may fail. Don't get discouraged.
It is better if it works in various environment without customization,
however it is hard work and is not main scope of the project.
Please read following instruction to modify settings to fit your environment.


Install
=======

You need to run setup.py(you can also do ``$ sudo make install`` )::

  $ sudo python setup.py develop

It it fail by lack of setuptools, try this::

   $ sudo apt-get install python-setuptools


Expected executables
====================

in case of plain Ubuntu 12.04
-----------------------------

'executable test' warns if expected executables aren't found.
When I tried it on Ubuntu 12.04 (2012-02-02), it said as follow

::
   $ python coderunner.py --exec-test
   check whether expected executables exist:
   Python
   /usr/bin/python2.7
   Ruby
   Test 'Ruby' expected executable named 'ruby1.9' in $PATH.
     install it or make symbolic link to it in coderunner/bin/
   Perl
   Test 'Perl' expected executable named 'perl5' in $PATH.
     install it or make symbolic link to it in coderunner/bin/
   JavaScript
   Test 'JS' expected executable named 'node' in $PATH.
     install it or make symbolic link to it in coderunner/bin/
   Scheme
   Test 'Scheme' expected executable named 'gosh' in $PATH.
     install it or make symbolic link to it in coderunner/bin/
   Java
   Test 'Java' expected executable named 'javac' in $PATH.
     install it or make symbolic link to it in coderunner/bin/
   C
   /usr/bin/gcc
   C++
   Test 'Cpp' expected executable named 'g++' in $PATH.
     install it or make symbolic link to it in coderunner/bin/
   C#
   Test 'CSharp' expected executable named 'gmcs' in $PATH.
     install it or make symbolic link to it in coderunner/bin/

So I did as follows

::
   $ sudo apt-get install ruby1.9.3 nodejs gauche openjdk-7-jdk g++ mono-gmcs
   $ cd bin
   $ ln -s /usr/bin/ruby1.9.3 ruby1.9
   $ ln -s /usr/bin/perl5.14.2 perl5



in case of Rackhub
------------------

I tried the test on `Rackhub`<http://rackhub.net/> (2012-06-10)
It warned as follow::

   coderunner$ python coderunner.py --exec-test
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

   $ sudo apt-get install gauche
   $ cd bin
   bin$ ln -s /home/rackhuber/.rvm/rubies/ruby-1.9.2-p320/bin/ruby ruby1.9
   bin$ ln -s /usr/bin/perl5.14.2 perl5

At that time I didn't support C# yet. Not using setup.py yet.


About Java7
===========

When I install Java7 on Mac OS X, it was installed in
/Library/Java/JavaVirtualMachines/1.7.0.jdk/Contents/Home/bin/java
`Oracle suggests to switch default jre using GUI<http://www.oracle.com/technetwork/java/javase/downloads/jdk-for-mac-readme-1564562.html>`_
, however I don't like it. I add another test runner which refer to 'java7' and 'javac7',
then put symbolic links in coderunner/bin/ .


::

   class Java7(Java):
       human_name = "Java7"
       pygments_name = "java7"
       bin = "javac7"


In Linux you can install as follows

::

   # Add the "WEBUPD8" PPA.
   $sudo add-apt-repository ppa:webupd8team/java
   $sudo apt-get update
   $sudo apt-get install oracle-java7-installer


About Smalltalk
===============

I installed squeak with Squeak-4.3-All-in-One.
It doesn't have ability to write stdout, so I installed OSProcess additionaly.
I made image with OSProcess. Though it takes 16MB, I didn't commit in the repository.
I hardcoded path of Squeak executable and the image in bin/run_squeak.py.
Please modify it as fit to your environment.

It may be better way to use gnu-smalltalk. On Ubuntu, apt-get install gnu-smalltalk works well.
On my Mac port install gst not works.


TODO
====

- It is too high hurdle for users to install all language beforehand.
  Test should be ignored when its prerequisite not satisfied.

  - current impl.: when _subproc failed with OSError, print error message and continue.
    It should be brushed up.

  - currently Smalltalk test call bin/run_squeak.py and fail in it.
    It is not trapped.

- To make output better, add heading between test? Add description to tests?
  http://nishio.github.com/learn_language/test_index.html

  - add 'description' on tests, add option to tell how to show it. (default: before code)
  - add 'Heading' class as a dummy tests. It is not good design.

- To make test case easily, helper script needed.

  - Input is a file which contains some codes separated with "\n----\n"
  - Output is a test script

- support Common Lisp, OCaml, etc.
