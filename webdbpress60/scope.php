<?php
$x = $y = 'global';
function foo(){
  global $y;
  echo "x: $x\n"; #-> x:
  echo "y: $y\n"; #-> y: global
}
foo();
