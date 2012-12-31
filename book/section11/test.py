# -*- encoding: utf-8 -*-
"""
Samples to cause error
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))
from coderunner.coderunner import *


test(Perl, """
# Perl
{
    package Counter;
    sub push{
        my $values = shift;
        $values->{count}++;
        print "$values->{count}匹\n";
    }
}

{
    # 引数にハッシュを渡す
    my $counter = {"value" => 0};
    my $c2 = {"value" => 0};

    Counter::push($counter);  #-> 1匹
    Counter::push($counter);  #-> 2匹
    Counter::push($c2);       #-> 1匹
    Counter::push($counter);  #-> 3匹
    Counter::push($c2);       #-> 2匹
}

""", """
1匹
2匹
1匹
3匹
2匹
""")

test(Perl, """
# Perl
{
    package Counter;
    sub new{
        return {"value" => 0};
    }
    sub push{
        my $values = shift;
        $values->{count}++;
        print "$values->{count}匹\n";
    }
}

{
    # 引数にハッシュを渡す
    my $counter = Counter::new;
    my $c2 = Counter::new;

    Counter::push($counter);  #-> 1匹
    Counter::push($counter);  #-> 2匹
    Counter::push($c2);       #-> 1匹
    Counter::push($counter);  #-> 3匹
    Counter::push($c2);       #-> 2匹
}
""", """
1匹
2匹
1匹
3匹
2匹
""")

main()

