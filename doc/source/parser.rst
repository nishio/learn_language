===================
 Parser on browser
===================

Demo
====


.. raw:: html

   <script src="repos/Parser-on-browser/eparse.js"></script>
   <script src="repos/Parser-on-browser/jquery-1.7.2.min.js"></script>
   <script src="repos/Parser-on-browser/jquery.terminal-0.4.15.js"></script>
   <script src="repos/Parser-on-browser/eparse.js"></script>
   <script src="repos/Parser-on-browser/eparse-test.js"></script>
   <link rel="stylesheet" type="text/css" href="repos/Parser-on-browser/terminal.css" />
   <script>
     $(function() {
       eparse.interface($('#term'), $('#operators'), $('#load'));
       eparse.test();
       $('body').click(function() { eparse.terminal.disable(); });
       $('#clear').click(function () { eparse.terminal.clear(); });
     });
   </script>

   <div id="term" style="width: 48%; height: 300px; float: left;"></div>
   <div style="width: 48%; float: right;">
       <textarea id="operators" style="width: 100%; height: 300px;">
   // define operators here
   // arguments: name, priority (>0), associativity ('left', 'right')

   operator('+', 1, 'left');
   operator('-', 1, 'left');
   operator('*', 2, 'left');
   operator('/', 2, 'left');
   operator('**', 3, 'right');
   </textarea>
       <input type="button" id="clear" value="Clear terminal" />
       <input type="button" id="load" value="Load operators" />
   </div>
   <p style="clear: both"></p>


Feature
=======

- The operator table is editable by the user in a textbox, for example:

::

   // define operators here
   // arguments: name, priority (>0), associativity ('left', 'right')

   operator('+', 1, 'left');
   operator('^', 3, 'left');
   operator('-', 1, 'left');
   operator('*', 2, 'left');
   operator('/', 2, 'left');
   operator('**', 3, 'right');


- The parser understand '(' ')'

- The user input an expression and receive a list of tokens, then the parser result, for example:

::

   eparse> 2+2*2**2**2*2+2
   tokens: [number(2), op(+), number(2), op(*), number(2), op(**), number
   (2), op(**), number(2), op(*), number(2), op(+), number(2)]
   result: [[2 + [[2 * [2 ** [2 ** 2]]] * 2]] + 2]


Read code!
==========

Its parser is about 200 lines.

https://github.com/nishio/Parser-on-browser


License
=======

GPLv3


Thanks
======

Paweł Marczewski wrote almost codes.
