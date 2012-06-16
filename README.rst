================
 Learn Language
================

To run and read codes helps you to learn language's core concept.

Preface
=======

Hi, I'm `Dr. NISHIO Hirokazu <http://www.nishiohirokazu.org/>`_.
I'm writing a book to teach the core concept of programming languages.
In the process, I feel some needs.

- To run a bunch of small codes and check its output.
  When I teach programming I use a lot of small codes.
  However sometimes their outputs changes depends on languages' version or enviroment settings.
  To make easy to check output, the input and output should be described in a runnable form.
  They are tests, in meaning of test-driven development.
  What I need is regression tests for textbook.

- To run codes helps you understand language's behavior.
  To read implementation of languages also helps you.
  However I found some problem when I writing my book.
  For some old languages, there are no easy way to ready to run.
  For some new languages, they are already grew too big to read.
  One way to overcome these problems are implement small subset of languages which run on browsers.


Project
=======

Notice these projects are on going and not completed nor stable yet.

- coderunner:
  tool to run codes and check their output

- doc:
  tool to make html files on
  http://nishio.github.com/learn_language/
  from test codes

- languages on browsers(under development)

  - https://github.com/nishio/LISP-on-browser
  - https://github.com/nishio/LazyK-on-browser
  - https://github.com/nishio/Brainfxck-on-browser
  - https://github.com/nishio/EDSAC-on-browser

For detail visit each project page

.. toctree::



License
=======

All test codes for coderunner are under these license:

- If no arthor are specified, it is public domain.
- If some arthor are specified, it is CC-BY 2.0.

Its purpose is not to disturb reader's work.

Tools (coderunner, sphinxdoc) are under GPLv3.
It is to ensure reusability of codes
even if I give up to maintain this projects.


How to contribute
=================

I greatly appreciate your contribution.
You can contact me by e-mail: nishio (dot) hirokazu (at) gmain (dot) com.
Or simply use pull-request of github.


Thanks
======

tokibito, aodag, moriyoshi, Dragan Zivkovic


