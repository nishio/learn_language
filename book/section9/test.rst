Python2.7
=========

.. code-block:: python

  # -*- encoding: utf-8 -*-
  def print_hex(s):
      print " ".join("%x" % ord(c) for c in s)
  
  x = u"aaaああ能aa\\$"
  
  print "JIS"
  print_hex(x.encode('iso-2022-jp'))
  print "SJIS"
  print_hex(x.encode('sjis'))
  print "EUC"
  print_hex(x.encode('euc-jp'))

::

  JIS
  61 61 61 1b 24 42 24 22 24 22 47 3d 1b 28 42 61 61 5c 24
  SJIS
  61 61 61 82 a0 82 a0 94 5c 61 61 5c 24
  EUC
  61 61 61 a4 a2 a4 a2 c7 bd 61 61 5c 24


Python2.7
=========

.. code-block:: python

  # -*- encoding: utf-8 -*-
  def print_hex(s):
      print " ".join("%x" % ord(c) for c in s)
  
  x = u"aaaあああaaa"
  
  print "JIS"
  print_hex(x.encode('iso-2022-jp'))
  print "SJIS"
  print_hex(x.encode('sjis'))
  print "EUC"
  print_hex(x.encode('euc-jp'))

::

  JIS
  61 61 61 1b 24 42 24 22 24 22 24 22 1b 28 42 61 61 61
  SJIS
  61 61 61 82 a0 82 a0 82 a0 61 61 61
  EUC
  61 61 61 a4 a2 a4 a2 a4 a2 61 61 61


Python2.7
=========

.. code-block:: python

  # -*- encoding: utf-8 -*-
  print '$"$"$"'.decode('iso-2022-jp')
  print '\x1b$B$"$"$"'.decode('iso-2022-jp').encode('utf-8')

::

  $"$"$"
  あああ


Python2.7
=========

.. code-block:: python

  # 日本語でコメントを書いただけ

::

    File "tmp.py", line 1
  SyntaxError: Non-ASCII character '\xe6' in file tmp.py on line 1, but no encoding declared; see http://www.python.org/peps/pep-0263.html for details


Python2.7
=========

.. code-block:: python

  # -*- encoding: utf-8 -*-
  
  # 日本語でコメントを書いただけ

::

  (no output)


C
=

.. code-block:: c

  #include <stdio.h>
  #include <string.h>
  
  int main(){
    char str[100] = "abc\0def";
    printf("%s\n", str);
    printf("%zu\n", strlen(str));
    return 0;
  }

::

  abc
  3


C++
===

.. code-block:: cpp

  #include <stdio.h>
  
  int main(){
    printf("1\n");
    // �����R�����g�̗�F����@�\
    printf("2\n");
    printf("3\n");
  }

::

  1
  3


C
=

.. code-block:: c

  #include <stdio.h>
  #include <string.h>
  
  int main(){
    int x = 9252;
    char str[3] = "abc";
    char str2[3] = "defg";
    printf("%s\n", str2);
    printf("%zu\n", strlen(str2));
    return 0;
  }

::

  defabc$$
  8


C
=

.. code-block:: c

  #include <stdio.h>
  
  int main(){
    printf("ドレミファソラシド\n");
  }

::

  ドレミファャ宴Vド


Perl
====

.. code-block:: perl

  print("ドレミファソラシド\n");
  print("表示\n");
  print("申し込む\n");

::

  ドレミファャ宴Vド
  侮ｦ
  垂ｵ込む


Perl
====

.. code-block:: perl

  print("図表");

::

  Can't find string terminator '"' anywhere before EOF at sjis2.pl line 1.




Perlではコメント中の\が改行をエスケープしないので2がコメントアウトされない


Perl
====

.. code-block:: perl

  print("1\n");
  # なになにの機能
  print("2\n");
  print("3\n");

::

  1
  2
  3


