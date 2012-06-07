use strict;
use warnings;
{
    package Bar;
    use Foo;
    @Bar::ISA = qw(Foo);
}
{
my $x = Bar->new;

print $x;
}
