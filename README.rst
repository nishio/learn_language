================
 Learn Language
================

To run and read codes helps you to learn language's core concept.


Preface
=======

Hi, I'm `Dr. NISHIO Hirokazu <http://www.nishiohirokazu.org/>`_.
I'm writing a book to teach the core concepts of programming languages.

I think that to run codes helps you understand language's behavior.
To read implementation of languages also helps you.
However, there are some problems:

- For some old languages, it is not easy to make environment you can run codes.
- For some new languages, it is already grew too big to read. It is not easy to understand.

One way to overcome these problems are implement small subset of languages which run on browsers.


Project
=======

- languages on browsers

  :Parser-on-browser:
     The concept of parser is very important. It is a recursive descent parser of infix notation works on browser. You can change and observe operators' priority and associativity.

  :LISP-on-browser:
     LISP is a language with simple but extensible grammers. You can try LISP on browser and learn how macros works.

  :AST-Visualization-on-browser: The concept of abstract syntax tree (AST) is very important. It is a visualizer which show AST of JavaScript in realtime. (it is better to change tree layout engine)

  :FORTH-on-browser: FORTH is a language with simple grammers and stack-based execution. The concept of stack-based execution is important because a lot of modern language (such as Java, Python and Ruby) choose it for thier implementation of virtual machine. (completed)

  :EDSAC-on-browser: EDSAC is a computer in 1950s. It allows us to make program with human-readable symbols instead of describing machine instructions as a bunch of bits. It is very primitive computer language.

  :Brainfxck-on-browser: Very small language with interesting architecture, which was inspired by the turing machine. (completed, but should be improved)

  :LazyK-on-browser: Lazy K is small *functional* language. (not yet)


- coderunner:

  - Tool to run codes and check their output.
    To run a bunch of small codes and check its output is important.
    When I teach programming I use a lot of small codes.
    However sometimes their outputs changes depends on languages' version or enviroment settings.
    To make easy to check output, the input and output should be described in a runnable form.
    They are tests, in meaning of test-driven development.
    What I need is regression tests for textbook.


- doc:

  - tool to make html files from test codes.
    The generated htmls are on
    http://nishio.github.com/learn_language/


For detail visit each project page

.. toctree



License
=======

All test codes for coderunner are under these license:

- If no arthor are specified, it is public domain.
- If no license are specified and some arthors are specified, it is CC-BY 2.0.

Its purpose is not to disturb reader's work.

Tools (coderunner, sphinxdoc) and languages are under GPLv3.
It is to ensure reusability of codes
even if I give up to maintain this projects.

TODO
====

- Python bytecode and st and ast visualizer
- (for ASTVIZ) Use better Tree layouting algorithm (implemented in LazyK project)
- SPIM (MIPS simulator) on browser?

How to contribute
=================

I greatly appreciate your contribution.
You can contact me by e-mail: nishio (dot) hirokazu (at) gmain (dot) com.
Or simply use pull-request of github.


Thanks
======

tokibito, aodag, moriyoshi, Dragan Zivkovic, Sri Ariyani


TODO
====

- Python AST visualizer and bytecode viewer
