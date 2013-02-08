Ruby
====

.. code-block:: ruby

  x = "Ruby"
  z = x
  x[0] = "P"
  p x #=> "Puby"
  p z #=> "Puby"

::

  "Puby"
  "Puby"


Perl
====

.. code-block:: perl

  # Perl
  $x = "global";
  
  sub yobu{
      local $x = "yobu";
      &yobareru();
  }
  
  sub yobareru{
      print "$x\n";
      # ↑「yobu」と表示される
  }
  
  &yobu();

::

  yobu




呼ばれる側でlocal宣言すると、新しい空の変数が作らる。thanks @__gfx__


Perl
====

.. code-block:: perl

  # Perl
  $x = "global";
  
  sub yobu{
      local $x;
      $x = "yobu";
      &yobareru();
  }
  
  sub yobareru{
      local $x;
      print "[$x]\n";
      # ↑[]と表示される
  }
  
  &yobu();

::

  []


Perl
====

.. code-block:: perl

  $x = "global";
  
  sub yobu{
      my $x = "yobu"; # ここをlocalからmyに変更した
      &yobareru();
  }
  
  sub yobareru{
      print "$x
  ";
      # ↑「global」と表示される
  }
  
  &yobu();

::

  global



from Ruby 1.9 block arguments has block scope
=============================================

Ruby1.8
=======

.. code-block:: ruby

  x = 0
  lambda {|x|}.call 1
  p x

::

  1


Ruby1.9
=======

.. code-block:: ruby

  x = 0
  lambda {|x|}.call 1
  p x

::

  0


Ruby
====

.. code-block:: ruby

  def foo()
    x = "outside"
    def bar()     # nested method
      p x         #-> raise error
    end
    bar()
  end
  
  foo()

::

  tmp.rb:4:in `bar': undefined local variable or method `x' for main:Object (NameError)
  	from tmp.rb:6:in `foo'
  	from tmp.rb:9:in `<main>'


Ruby
====

.. code-block:: ruby

  def foo()
      x = "old"  # name 'x' is in the scope of foo-method
      lambda {x = "new"; y = "new"}.call
      # ↑x is foo's and y is lambda's local variable
      p x  #-> x was changed to "new"
      p y  #-> raise error: we can't see y because it is lambda's local variable
  end
  
  foo

::

  "new"
  tmp.rb:6:in `foo': undefined local variable or method `y' for main:Object (NameError)
  	from tmp.rb:9:in `<main>'



Python 3.0 has new 'nonlocal' declaration
=========================================

Python2.7
=========

.. code-block:: python

  def foo():
      x = "old"
      def bar():
          x = "new"
          # I want to rewrite 'x' in outer scope,
          # however it makes new local variable
      bar()
      print x
  
  foo() #-> old (not changed)

::

  old


Python3.0
=========

.. code-block:: python

  def foo():
      x = "old"
      def bar():
          nonlocal x  # daclare 'x' is not a local variable
          x = "new"   # rewrite 'x' in outer scope
      bar()
      print(x)
  
  foo()  #-> new (changed)

::

  new


