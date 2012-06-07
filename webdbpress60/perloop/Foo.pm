
package Foo;
sub push{
    print "Foo\n";
}
sub new{
    my $class = shift;
    bless {}, $class;
}
1;
