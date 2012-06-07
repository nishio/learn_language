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
# (1)引数にハッシュを渡す
my $counter = {"value" => 0}; 
my $c2 = {"value" => 0}; 

Counter::push($counter); #-> 1匹
Counter::push($counter); #-> 2匹
Counter::push($c2); #-> 1匹
Counter::push($counter); #-> 3匹
Counter::push($c2); #-> 2匹
}
