use strict;
use warnings;

{
    package Counter;
    sub push{
	my $values = shift;
	$values->{count}++;
	print "$values->{count}匹\n";
    }
    sub new{
	my $class = shift;
	my $values = {count => shift};
	bless $values, $class;
    }
}

{
# (1)引数にハッシュを渡す
my $counter = {"value" => 0}; 
print "$counter\n"; 
#-> HASH(0x1008001f0)
Counter::push($counter); #-> 1匹

# (2)ハッシュとパッケージを結びつける
bless $counter, "Counter";
print "$counter\n"; 
#-> Counter=HASH(0x1008001f0)
$counter->push; #-> 2匹

# (3)初期化の処理もパッケージに入れる
my $c2 = Counter->new;
$c2->push; #-> 1匹
$counter->push; #-> 3匹
}
