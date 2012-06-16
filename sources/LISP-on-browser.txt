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

- (done) Milestone1: S-expression Parser

  - given string such like "(* 1 (+ 2 3))" and return syntax trees
  - in this point forget about reader macros such as "'(1 2 3)"

- (done) Milestone2: Some Built-in function

  - arithmetic functions: +, -, \*, /
  - other functions: eval, cons, list

- (done) Milestone3: A REPL interpreter(when user input (* 1 (+ 2 3)), it prints 5)

  - Now we can (* 1 (+ 2 3))

- (done) Milestone4: Special forms: quote and if
- (done) Milestone5: Reader syntax with apostrophe: '(+ 2 2) = (quote (+ 2 2))


- Milestone6: equality and comparison: =, /=, <, etc.
- Milestone7: comments in the code
- Milestone8: a textbox for loading examples into interpreter

- Milestone9: lexical scope (let and variables)
- Milestone10: defining your own functions (defun)

 - Now we can make factorial and counter

- Further milestones (need to break into smaller milestones)

  - Strings, I/O (print, read) using terminal
  - Macros (and quasiquote/unquote)

::

   ; factorial
   (defun factorial (n) (if (= n 0) 1 (* n (factorial (- n 1)))))

   ; counter
   gosh> (define (counter)
     (let ((count 0))
        (lambda () (set! count (+ 1 count)))))
   counter
   gosh> (define c (counter))
   c
   gosh> (c)
   1
   gosh> (c)
   2
   gosh> (c)
   3


License
=======

GPLv3


Thanks
======

Paweł Marczewski wrote almost codes.
