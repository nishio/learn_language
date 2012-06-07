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
# (3)初期化の処理もパッケージに入れる
my $c1 = Counter->new;
my $c2 = Counter->new;
$c1->push; #-> 1匹
$c2->push; #-> 1匹
$c1->push; #-> 2匹
}
