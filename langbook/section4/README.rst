

C
-----

.. code-block:: c

  #include <stdio.h>
  
  void use_for(){
    printf("use_for\n");
    int N = 5;
    int i;
    for(i = 0; i < N; i++){
      printf("%d\n", i);
    }
  }
  
  void not_use_for(){
    printf("not_use_for\n");
    int N = 5;
    int i;
    i = 0;
    while(i < N){
      printf("%d\n", i);
      i++;
    }
  }
  
  int main(int argc, char** argv){
    use_for();
    not_use_for();
  }


::

  use_for
  0
  1
  2
  3
  4
  not_use_for
  0
  1
  2
  3
  4



C
-----

.. code-block:: c

  #include <stdio.h>
  void use_while(int x){
    printf("use_while\n");
    while(x > 0){
      printf("%d\n", x);
      x--;
    }
  }
  
  void not_use_while(int x){
    printf("not_use_while\n");
   START_LOOP:
    if(!(x > 0)) goto END_LOOP;
    printf("%d\n", x);
    x--;
    goto START_LOOP;
   END_LOOP:
    return;
  }
  
  int main(){
    use_while(5);
    not_use_while(5);
  }


::

  use_while
  5
  4
  3
  2
  1
  not_use_while
  5
  4
  3
  2
  1



C
-----

.. code-block:: c

  #include <stdio.h>
  void use_if(int x){
    if(x > 0){
      printf("正の数\n");
    }else if(x < 0){
      printf("負の数\n");
    }else{
      printf("ゼロ\n");
    }
  }
  
  void not_use_if(int x){
    if(x <= 0) goto NOT_POSITIVE;
    printf("正の数\n");
    goto END;
   NOT_POSITIVE:
    if(x >= 0) goto NOT_NEGATIVE;
    printf("負の数\n");
    goto END;
   NOT_NEGATIVE:
    printf("ゼロ\n");
   END:
    return;
  }
  
  int main(){
    use_if(-1);
    use_if(0);
    use_if(1);
    not_use_if(-1);
    not_use_if(0);
    not_use_if(1);
  }


::

  負の数
  ゼロ
  正の数
  負の数
  ゼロ
  正の数



Java
-----

.. code-block:: java

  import java.util.Iterator;
  import java.util.List;
  import java.util.Arrays;
  
  class ForLoopTest{
      public static void main(String[] args){
          int[] items = new int[]{1, 2, 3, 4, 5};
  
          System.out.println("C style for-loop");
          for(int i = 0; i < items.length; i++){
              int item = items[i];
              System.out.println(item);
          }
  
          System.out.println("Iterator for-loop");
          List<Integer> items2 = Arrays.asList(new Integer[]{1, 2, 3, 4, 5});
          for (Iterator<Integer> i = items2.iterator(); i.hasNext(); ){
              int item = i.next();
              System.out.println(item);
          }
  
          System.out.println("For-each loop");
          // http://docs.oracle.com/javase/1.5.0/docs/guide/language/foreach.html
          for(int item: items){
              System.out.println(item);
          }
      }
  }


::

  C style for-loop
  1
  2
  3
  4
  5
  Iterator for-loop
  1
  2
  3
  4
  5
  For-each loop
  1
  2
  3
  4
  5

