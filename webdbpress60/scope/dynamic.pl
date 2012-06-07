#use strict;
use warnings;

$x = "global";

sub yobu{
    local $x;
    $x = "yobu-local";
    &yobareru();
}

sub yobareru{
    
    print "$x\n";
    # ↑「yoku-local」と表示される
}

&yobu();
