

Python
------

.. code-block:: python

  class Parent:
      x = "A"
  
  print Parent.x #-> A
  
  class Child(Parent):
      pass
  
  print Child.x #-> A


::

  A
  A



Python
------

.. code-block:: python

  class ParentA:
      x = "A"
  
  class ParentB:
      x = "B"
  
  class Child(ParentA, ParentB):
      pass
  
  print Child.x


::

  A



Python
------

.. code-block:: python

  class Parent:
      x = "A"
  
  class Child(Parent):
      x = "B"
  
  print Child.x


::

  B



Python
------

.. code-block:: python

  class Base:
      x = "A"
  
  class Derived1(Base):
      pass
  
  class Derived2(Base):
      x = "B"
  
  class Multi(Derived1, Derived2):
      pass
  
  print Multi.x


::

  A



Python
------

.. code-block:: python

  class Base(object):
      x = "A"
  
  class Derived1(Base):
      pass
  
  class Derived2(Base):
      x = "B"
  
  class Multi(Derived1, Derived2):
      pass
  
  print Multi.x


::

  B



Ruby
-----

.. code-block:: ruby

  # Ruby
  module Hello
    def hello
      puts "hello!"
    end
  end
  
  module Bye
    def bye
      puts "bye!"
    end
  end
  
  class Greeting
    include Hello
    include Bye
  end
  
  Greeting.new.hello  #-> hello!
  Greeting.new.bye    #-> bye!


::

  hello!
  bye!



Ruby1.9
-------

.. code-block:: ruby

  # Ruby
  module Foo
    def hello
      puts "foo!"
    end
  end
  
  module Bar
    def hello
      puts "bar!"
    end
  end
  
  class Foobar
    include Foo
    include Bar
  end
  
  class Barfoo
    include Bar
    include Foo
  end
  
  Foobar.new.hello   #-> bar!
  Barfoo.new.hello   #-> foo!


::

  bar!
  foo!

