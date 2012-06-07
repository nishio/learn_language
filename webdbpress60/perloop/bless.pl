{
    package Counter;
    sub push{
	$values = shift;
	$values->{count}++;
	print "$values->{count}匹\n";
    }
}

$counter = {"value" => 0}; 
print "$counter\n"; # HASH(0x1008001f0)

bless $counter, Counter;
print "$counter\n"; # Counter=HASH(0x1008001f0)

$counter->push; # 1匹
$counter->push; # 2匹
