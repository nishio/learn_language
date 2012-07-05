======================
 Brainf*ck on browser
======================

Demo
====

.. raw:: html

   <link href="repos/Brainfxck-on-Browser/bootstrap/css/bootstrap.min.css" rel="stylesheet">
   <script src="repos/Brainfxck-on-Browser/bootstrap/js/bootstrap.min.js"></script>
   <link href="repos/Brainfxck-on-Browser/style.css" rel="stylesheet">
   <!-- Le HTML5 shim, for IE6-8 support of HTML5 elements -->
   <!--[if lt IE 9]>
       <script src="http://html5shim.googlecode.com/svn/trunk/html5.js"></script>
   <![endif]-->
   <script src="repos/Brainfxck-on-Browser/jquery.js"></script>
   <script src="repos/Brainfxck-on-Browser/trybf-utils.js"></script>
   <script src="repos/Brainfxck-on-Browser/trybf-memory.js"></script>
   <script src="repos/Brainfxck-on-Browser/trybf.js"></script>

   <div class="navbar navbar-fixed-top">
       <div class="navbar-inner">
           <div class="container">
               <ul class="nav">
                   <li class="active">
                       <a href="index.html">Home</a>
                   </li>
                   <li>
                       <a href="readme.html">Readme</a>
                   </li>
               </ul>
           </div>
       </div>
   </div>

   <div class="container-fluid" id="bf">
       <div id="edit" class="row">
           <div class="span6">
               <h4>Program</h4>
               <textarea id="code" class="span6" style="height:300px;"></textarea>

               <div class="btn-group" id="edit-mode">
                   <button id="run" class="btn" title="Run program">
                       <i class="icon-play"></i>
                   </button>
                   <button id="debug" class="btn" title="Start debugging">
                       <i class="icon-asterisk"></i>
                   </button>
               </div>

               <div class="btn-group" id="run-mode" hidden>
                   <button id="stop" class="btn" title="Stop program running">
                           <i class="icon-stop"></i>
                   </button>
               </div>

               <div class="btn-group" id="debug-mode" hidden>
                   <button id="stop" class="btn" title="Stop debugging">
                       <i class="icon-stop"></i>
                   </button>
                   <button id="step" class="btn" title="Go to next instruction">
                       <i class="icon-step-forward"></i>
                   </button>
                   <button id="stepto" class="btn" title="Go to next (breakpoint)">
                       <i class="icon-fast-forward"></i>
                   </button>
               </div>
           </div>

           <div class="span6">
               <h4>Memory</h4>
               <pre id="mem"></pre>
               <h4>Output</h4>
               <pre id="output"></pre>
           </div>
       </div>
   </div>

   <p style="clear: both; height 2em;"> </p>


Feature
=======

Brainf*ck interpreter which run on browsers.


License
=======

GPLv3


Thanks
======

Artem Smirnov wrote almost codes.

