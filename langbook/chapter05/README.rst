

Python
------

.. code-block:: python

  # -*- encoding: utf-8 -*-
  def total(xs):
      result = 0
      for x in xs:
          if is_integer(x):
              result += x
          else:
              # xはリストなのでtotalで中身を合計する！
              result += total(x)
  
      return result
  
  
  def is_integer(x):
      return isinstance(x, int)
  
  
  print total([1, 2, [3, 4], 5])


::

  15

