

Python3.0
---------

.. code-block:: python

  print(oct(1000))  #=> '0o1750'
  print(0o1750)
  print(hex(1000))  #=> '0x3e8'
  print(0x3e8)


::

  0o1750
  1000
  0x3e8
  1000



JavaScript
----------

.. code-block:: javascript

  console.log(0.3 + 0.3 + 0.3 + 0.3 + 0.3 + 0.3 + 0.3 + 0.3 + 0.3 + 0.3)
  console.log(Math.floor(0.3 + 0.3 + 0.3 + 0.3 + 0.3 + 0.3 + 0.3 + 0.3 + 0.3 + 0.3))


::

  2.9999999999999996
  2



C
-----

.. code-block:: c

  #include <stdio.h>
  
  float divide_int(int x){
    return x / 2;
  }
  
  float divide_float(float x){
    return x / 2;
  }
  
  int main(){
    printf("%f\n", divide_int(1));
    printf("%f\n", divide_float(1));
  }


::

  0.000000
  0.500000



Python2.7
---------

.. code-block:: python

  print 1 / 2
  print 1 // 2


::

  0
  0



Python3.0
---------

.. code-block:: python

  print(1 / 2)
  print(1 // 2)


::

  0.5
  0



Haskell
-------

.. code-block:: haskell

  data Person a = MakePerson {age :: Int, name :: String, something :: a}
  
  x :: Person Int
  x = MakePerson {age = 31, name = "nishio", something = 1}
  
  y :: Person String
  y = MakePerson {age = 31, name = "nishio", something = "hoge"}
  
  main = do
    print $ something x   -- -> 1
    print $ something y   -- -> "hoge"


::

  1
  "hoge"



Haskell
-------

::

  Prelude> let add_one = \x -> x + 1
  Prelude> :type add_one
  add_one :: Integer -> Integer



Haskell
-------

::

  Prelude> let identity = \x -> x
  Prelude> :type identity
  identity :: t -> t
  Prelude> :type identity identity
  identity identity :: t -> t
  Prelude> identity identity 1
  1



Scala
-----

::

  scala> def identity = x => x
  <console>:7: error: missing parameter type
         def identity = x => x
                        ^



Scala
-----

::

  scala> def identity[T] = (x : T) => x
  identity: [T]=> T => T
  
  scala> identity(identity)
  res0: Nothing => Nothing = <function1>
  
  scala> identity(identity)(1)
  <console>:9: error: type mismatch;
   found   : Int(1)
   required: Nothing
                identity(identity)(1)
                                   ^

