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






