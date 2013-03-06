
trait can't be instanciated
===========================

Scala
=====

.. code-block:: scala

  trait Foo{
    def foo() = println("foo!")
  }
  
  new Foo  // error

::

  ...tmp.scala:5: error: trait Foo is abstract; cannot be instantiated
  new Foo  // error
  ^
  one error found


Scala
=====

.. code-block:: scala

  trait Foo{
    def foo() = println("foo!")
  }
  
  class C extends Foo{}
  new C().foo

::

  foo!


Scala
=====

.. code-block:: scala

  trait Foo{
    def foo() = println("foo!")
  }
  
  trait Bar{
    def bar() = println("bar!")
  }
  
  class C extends Foo with Bar{}
  new C().foo
  new C().bar

::

  foo!
  bar!



conflicting name
================

Scala
=====

.. code-block:: scala

  trait Foo{
    def hello() = println("foo!")
  }
  
  trait Bar{
    def hello() = println("bar!")
  }
  
  class C extends Foo with Bar{}

::

  ...tmp.scala:9: error: class C inherits conflicting members:
    method hello in trait Foo of type ()Unit  and
    method hello in trait Bar of type ()Unit
  (Note: this can be resolved by declaring an override in class C.)
  class C extends Foo with Bar{}
        ^
  one error found


Scala
=====

.. code-block:: scala

  trait Foo{
    def hello() = println("foo!")
  }
  
  trait Bar{
    def hello() = println("bar!")
  }
  
  class C extends Foo with Bar{
    override def hello() = super[Foo].hello
  }
  
  new C().hello

::

  foo!


Scala
=====

.. code-block:: scala

  trait Foo{
    def hello() = println("foo!")
  }
  
  trait Bar{
    def hello() = println("bar!")
  }
  
  class C extends Foo with Bar{
    override def hello() = {  // use both
      super[Foo].hello
      super[Bar].hello
    }
  }
  
  new C().hello

::

  foo!
  bar!



required trait(self type annotation)
====================================

Scala
=====

.. code-block:: scala

  trait HaveFoo{
    def foo() : String = "foo"
  }
  
  trait NeedFoo{
    self : HaveFoo =>
    def hello() = println(foo())
  }
  
  // error: NeedFoo should be with HaveFoo
  class C extends NeedFoo{}

::

  ...tmp.scala:11: error: illegal inheritance;
   self-type this.C does not conform to this.NeedFoo's selftype this.NeedFoo with this.HaveFoo
  class C extends NeedFoo{}
                  ^
  one error found


Scala
=====

.. code-block:: scala

  trait HaveFoo{
    def foo() : String = "foo"
  }
  
  trait NeedFoo{
    self : HaveFoo =>
    def hello() = println(foo())
  }
  
  class C extends NeedFoo with HaveFoo{}
  new C().hello

::

  foo


