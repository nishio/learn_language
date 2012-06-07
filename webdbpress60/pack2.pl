{
    package Counter;
    my $count = 0;
    my $name = "スズメ";

    sub push{
	my $values = shift;
	$values->{count}++;
	print "$name: $values->{count}匹\n";
    }
    sub reset{
	my $values = shift;
	$count = 0;
	print "$name: リセット\n";
    }
}

$value1 = {"count" => 0};
$value2 = {"count" => 0};
Counter::push($value1); #-> スズメ: 1匹
Counter::push($value1); #-> スズメ: 2匹
Counter::push($value1); #-> スズメ: 3匹
Counter::reset($value1); #-> スズメ: リセット
Counter::push($value1); #-> スズメ: 1匹






