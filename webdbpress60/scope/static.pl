#use strict;
use warnings;

$x = "global";

sub yobu{
    my $x; # ここをlocalからmyに変更した
    $x = "yobu-local";
    &yobareru();
}

sub yobareru{
    print "$x\n";
    # ↑「global」と表示される
}

&yobu();
