use strict;
use warnings;

{
    package Counter;
    sub push{
	my $values = shift;
	$values->{count}++;
	print "$values->{count}匹\n";
    }
}

{

my $counter = {"value" => 0}; 
print "$counter\n"; 
#-> HASH(0x1008001f0) # 普通のハッシュ

# ハッシュとパッケージを結びつける
bless $counter, "Counter";
print "$counter\n"; 
#-> Counter=HASH(0x1008001f0)
# blessされたハッシュ
$counter->push; #-> 1匹
$counter->push; #-> 2匹
}
