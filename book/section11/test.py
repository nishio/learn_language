# -*- encoding: utf-8 -*-
"""
Samples to cause error
"""
from coderunner import *

test(Perl, """
# Perlのパッケージでカウンタを作る
{
    package Counter;
    my $count = 0;
    my $name = "スズメ";

    sub push{
        $count++;
        print "$name: $count匹\n";
    }
    sub reset{
        $count = 0;
        print "$name: リセット\n";
    }
}

Counter::push; #-> スズメ: 1匹
Counter::push; #-> スズメ: 2匹
Counter::push; #-> スズメ: 3匹
Counter::reset; #-> スズメ: リセット
Counter::push; #-> スズメ: 1匹
""", """
スズメ: 1匹
スズメ: 2匹
スズメ: 3匹
スズメ: リセット
スズメ: 1匹
""")


test(Perl, """
# Perl
{
    package Counter;
    sub push{
        my $values = shift;
        $values->{count}++;
        print "$values->{count}匹\n";
    }
}

{
    # ハッシュを作る
    my $counter = {"value" => 0};
    my $c2 = {"value" => 0};

    # 引数にハッシュを渡す
    Counter::push($counter);  #-> 1匹
    Counter::push($counter);  #-> 2匹
    Counter::push($c2);       #-> 1匹
    Counter::push($counter);  #-> 3匹
    Counter::push($c2);       #-> 2匹
}
""", """
1匹
2匹
1匹
3匹
2匹
""")

test(Perl, """
# Perl
{
    package Counter;
    sub new{
        return {"value" => 0};
    }
    sub push{
        my $values = shift;
        $values->{count}++;
        print "$values->{count}匹\n";
    }
}

{
    # 初期化の処理をパッケージに入れた
    my $counter = Counter::new;
    my $c2 = Counter::new;

    # 引数にハッシュを渡す
    Counter::push($counter);  #-> 1匹
    Counter::push($counter);  #-> 2匹
    Counter::push($c2);       #-> 1匹
    Counter::push($counter);  #-> 3匹
    Counter::push($c2);       #-> 2匹
}
""", """
1匹
2匹
1匹
3匹
2匹
""")


test(Perl, """
# Perl
{
    package Counter;
    sub new{
        return {"value" => 0};
    }
    sub push{
        my $values = shift;
        $values->{count}++;
        print "$values->{count}匹\n";
    }
}

{
    my $counter = {"value" => 0};
    print "$counter\n";
    #-> HASH(0x1008001f0)  # blessされてないハッシュ

    # ハッシュとパッケージを結び付ける
    bless $counter, "Counter";
    print "$counter\n";
    #-> Counter=HASH(0x1008001f0)
    # blessされたハッシュ

    $counter->push;  #-> 1匹 # 矢印演算子で手軽に使える！
    $counter->push;  #-> 2匹
}
""", """
HASH(0x1008001f0)
Counter=HASH(0x1008001f0)
1匹
2匹
""")
# 0x1008001f0は実行のたびに変わる値


test(Perl, """
# Perl
{
    package Counter;
    sub new{
        my $class = shift;
        my $values = {count => 0};
        bless $values, $class;
    }
    sub push{
        my $values = shift;
        $values->{count}++;
        print "$values->{count}匹\n";
    }
}

{
    # 初期化の処理をパッケージに入れた
    my $counter = Counter->new;
    my $c2 = Counter->new;

    # 引数にハッシュを渡す
    $counter->push;  #-> 1匹
    $counter->push;  #-> 2匹
    $c2->push;       #-> 1匹
    $counter->push;  #-> 3匹
    $c2->push;       #-> 2匹
}
""", """
1匹
2匹
1匹
3匹
2匹
""")

test(JS, """
// JavaScript
var counter = {
    count: 0,
    name: "スズメ",

    push: function(){
        this.count++;
        print(this.name + ": " +
                    this.count + "匹");
    },
    reset: function(){
        this.count = 0;
        print(this.name + ": " +
                    "リセット");
    }
}

counter.push(); //-> スズメ: 1匹
counter.push(); //-> スズメ: 2匹
counter.push(); //-> スズメ: 3匹
counter.reset();//-> スズメ: リセット
counter.push(); //-> スズメ: 1匹
""", """
スズメ: 1匹
スズメ: 2匹
スズメ: 3匹
スズメ: リセット
スズメ: 1匹
""")


test(JS, """
// JavaScript
function makeCounter(){
    return {
        count: 0,
        push: function(){
            this.count++;
            print(this.count + "匹");
        }
    }
}

var c1 = makeCounter();
var c2 = makeCounter();
c1.push(); //-> 1匹
c2.push(); //-> 1匹
c1.push(); //-> 2匹
""", """
1匹
1匹
2匹
""")

test(JS, """
// JavaScript
function Foo(){
    this.x = 1
}
Foo.prototype.y = 2
var obj = new Foo();
print(obj); // -> Object {x=1, more...}
print(obj.__proto__); // -> Object {y=2}
print(obj.x); // -> 1
print(obj.y); // -> 2
""", """
[object Object]
[object Object]
1
2
""") # Rhinoだとオブジェクトの区別がつかない

test(JS, """
// JavaScript
var Counter = function() {
    this.count = 0;
}

Counter.prototype.push = function(){
    this.count++;
    print(this.count + "匹");
}

var c1 = new Counter();
c1.push(); //-> 1匹
c1.push(); //-> 2匹
var c2 = new Counter();
print(c1.push === c2.push) //-> true // 同じ物
""", """
1匹
2匹
true
""")

test(JS, """
// JavaScript
function makeCounter(){
  var count = 0;
  function push(){
    count++;
    print(count);
  }
  return push;
}

c = makeCounter();
c(); c(); c();
""", """
1
2
3
""")

main()

