sub foo{
    my $x = "m";
    sub bar{
	$x = 0;
    }
    &bar();
    print "$x\n";
}

&foo();

