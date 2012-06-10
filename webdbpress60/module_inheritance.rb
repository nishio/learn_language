module Foo
  def hello
    puts "hello"
  end
  module_function :hello
end

module Bar
  def hello
    Foo.hello
    Foo.hello
  end
  module_function :hello
end

Bar.hello
