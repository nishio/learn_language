=================
 LISP on browser
=================

This is small implementation of LISP,
which written in JavaScript and run on browsers.

I think it helps you to understand what goint on in programming languages
by using it and reading its source codes.


Design
======

Readability counts.

My goal is not to make complete features of Lisp.
It makes source codes huge and makes difficult to read.


TODO
====

- Refactor commit history so that readers can learn how to implement LISP step by step.
  'feature/M1-S-Expression-Parser' branch is nice but 'feature/M2' has actually 4 milestone.

- Connect with https://github.com/nishio/AST-Visualization-on-browser

- Make a site in English and Japanese (for my book's readers)

History
=======

This list corresponds to current commit history. We need refactor it.

- Milestone1: S-expression Parser

  - given string such like "(* 1 (+ 2 3))" and return syntax trees
  - in this point forget about reader macros such as "'(1 2 3)"

- 'feature/M2'

  - Milestone2: Some Built-in function

    - arithmetic functions: +, -, \*, /
    - other functions: eval, cons, list

  - (done) Milestone3: A REPL interpreter(when user input (* 1 (+ 2 3)), it prints 5)

    - Now we can (* 1 (+ 2 3))

  - (done) Milestone4: Special forms: quote and if
  - (done) Milestone5: Reader syntax with apostrophe: '(+ 2 2) = (quote (+ 2 2))

- 'feature/factorial_and_counter'

  - Milestone6: equality and comparison: =, /=, <, etc.
  - Milestone7: comments in the code
  - Milestone8: a textbox for loading examples into interpreter

  - Milestone9: lexical scope (let and variables)
  - Milestone10: defining your own functions (defun)

    - Now we can make factorial and counter

- 'feature/macro'

  - variable-length argument lists (func arg1 arg2 . rest)
  - defmacro and macro-expansion stage
  - macroexpand function
  - quasiquote and unquote (` ,) for easier building of macros
  - a 'gensym' function and example illustrating the problem of hygiene in macros.


License
=======

GPLv3


Thanks
======

Paweł Marczewski wrote almost codes.
