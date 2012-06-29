=======
 repos
=======

Directory to put other repositories:

::

   git clone https://github.com/nishio/Parser-on-browser.git


how to add project
==================

- git clone in this dir
- make *.rst, using ".. raw:: html" directive
- path to scripts and stylesheets are "repos/<repos_name>/<filename>"
- I did "cd build/html; ln -s ../../repos" so you can see it works on build/html
- Add the rst to toctree
- deploy (yet to be write)
