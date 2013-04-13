# -*- encoding: utf-8 -*-
"""
Samples to cause error
"""
from coderunner import *

test(Java, "TestDelegate.java", is_file=True, is_embedded_output=True)
test(Java, "TestMultiImpl.java", is_file=True, to_run=False)
test(Java, "TestMultiImpl2.java", is_file=True, to_run=False)
drop_tests()

test(Python, """
class Parent:
    x = "A"

print Parent.x #-> A

class Child(Parent):
    pass

print Child.x #-> A
""", """
A
A
""")


test(Python, """
class ParentA:
    x = "A"

class ParentB:
    x = "B"

class Child(ParentA, ParentB):
    pass

print Child.x
""", """
A
""")

test(Python, """
class Parent:
    x = "A"

class Child(Parent):
    x = "B"

print Child.x
""", """
B
""")

test(Python, """
class Base:
    x = "A"

class Derived1(Base):
    pass

class Derived2(Base):
    x = "B"

class Multi(Derived1, Derived2):
    pass

print Multi.x
""", """
A
""")


test(Python, """
class Base(object):
    x = "A"

class Derived1(Base):
    pass

class Derived2(Base):
    x = "B"

class Multi(Derived1, Derived2):
    pass

print Multi.x
""", """
B
""")


test(Ruby, """
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
""", """
hello!
bye!
""")

test(Ruby19, """
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
""", """
bar!
foo!
""")


if __name__ == '__main__':
    main()

