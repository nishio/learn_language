

Python
------

.. code-block:: python

  import dis
  dis.dis(lambda x, y, z: (x + y) * z)


::

    2           0 LOAD_FAST                0 (x)
                3 LOAD_FAST                1 (y)
                6 BINARY_ADD          
                7 LOAD_FAST                2 (z)
               10 BINARY_MULTIPLY     
               11 RETURN_VALUE        



Python
------

.. code-block:: python

  import ast
  print ast.dump(ast.parse("1 + 2"))


::

  Module(body=[Expr(value=BinOp(left=Num(n=1), op=Add(), right=Num(n=2)))])



Python
------

.. code-block:: python

  import ast
  print ast.dump(ast.parse("(1 + 2) * 3"))


::

  Module(body=[Expr(value=BinOp(left=BinOp(left=Num(n=1), op=Add(), right=Num(n=2)), op=Mult(), right=Num(n=3)))])



C++
-----

.. code-block:: cpp

  #include <vector>
  using namespace std;
  
  int main(){
    // OK
    vector<vector<int> > x;
  }


::

  (no output)



C++
-----

.. code-block:: cpp

  #include <vector>
  using namespace std;
  
  int main(){
    // NG
    vector<vector<int>> x;
  }


::

  tmp.cpp: In function 'int main()':
  tmp.cpp:6: error: '>>' should be '> >' within a nested template argument list

