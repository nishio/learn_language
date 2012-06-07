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

Foobar.new.hello #-> bar!

