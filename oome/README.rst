==================
 OutOfMemoryError
==================

with ``-XX:PermSize=4m -XX:MaxPermSize=4m``

::
   Exception in thread "main" [Full GC [Tenured: 515K->515K(56960K), 0.0091940 secs] 973K->515K(82688K), [Perm : 4095K->4026K(4096K)], 0.0092350 secs] [Times: user=0.01 sys=0.00, real=0.00 secs]
   java.lang.OutOfMemoryError: PermGen space
           at java.lang.ClassLoader.defineClass1(Native Method)
           at java.lang.ClassLoader.defineClass(ClassLoader.java:791)
           at java.lang.ClassLoader.defineClass(ClassLoader.java:634)
           at Test.loadNext(Test.java:135)
           at Test.main(Test.java:142)
   Heap
    def new generation   total 25728K, used 916K [0x00000007bfc00000, 0x00000007c17e0000, 0x00000007d5150000)
     eden space 22912K,   4% used [0x00000007bfc00000, 0x00000007bfce52b8, 0x00000007c1260000)
     from space 2816K,   0% used [0x00000007c1260000, 0x00000007c1260000, 0x00000007c1520000)
     to   space 2816K,   0% used [0x00000007c1520000, 0x00000007c1520000, 0x00000007c17e0000)
    tenured generation   total 56960K, used 515K [0x00000007d5150000, 0x00000007d88f0000, 0x00000007ffc00000)
      the space 56960K,   0% used [0x00000007d5150000, 0x00000007d51d0e30, 0x00000007d51d1000, 0x00000007d88f0000)
    compacting perm gen  total 4096K, used 4058K [0x00000007ffc00000, 0x0000000800000000, 0x0000000800000000)
      the space 4096K,  99% used [0x00000007ffc00000, 0x00000007ffff6bd8, 0x00000007ffff6c00, 0x0000000800000000)



without ``-XX:PermSize=4m -XX:MaxPermSize=4m`` it takes much memory

::

   80679
   80680
   80681
   [Full GC [Tenured: 9233K->9547K(56768K), 0.2963840 secs] 16067K->9547K(82368K), [Perm : 83967K->83967K(83968K)], 0.2964300 secs] [Times: user=0.29 sys=0.00, real=0.30 secs] 
   [Full GC [Tenured: 9547K->9547K(56768K), 0.2902660 secs] 9547K->9547K(82368K), [Perm : 83967K->83967K(83968K)], 0.2903070 secs] [Times: user=0.28 sys=0.00, real=0.29 secs] 
   [Full GC [Tenured: 9547K->9547K(56768K), 0.3495300 secs] 9547K->9547K(82368K), [Perm : 83967K->83967K(83968K)], 0.3495820 secs] [Times: user=0.29 sys=0.00, real=0.35 secs] 
   [Full GC [Tenured: 9547K->9547K(56768K), 0.2926770 secs] 9547K->9547K(82368K), [Perm : 83967K->83967K(83968K)], 0.2928020 secs] [Times: user=0.28 sys=0.00, real=0.30 secs] 
   [Full GC [Tenured: 9547K->9539K(56768K), 0.3287100 secs] 9547K->9539K(82368K), [Perm : 83967K->83967K(83968K)], 0.3287660 secs] [Times: user=0.33 sys=0.01, real=0.33 secs] 
   [Full GC [Tenured: 9539K->9539K(56768K), 0.2849540 secs] 9539K->9539K(82368K), [Perm : 83967K->83967K(83968K)], 0.2849960 secs] [Times: user=0.27 sys=0.00, real=0.28 secs] 
   [Full GC [Tenured: 9539K->9539K(56768K), 0.2698740 secs] 9539K->9539K(82368K), [Perm : 83967K->83967K(83968K)], 0.2699230 secs] [Times: user=0.26 sys=0.00, real=0.27 secs] 
   Exception in thread "main" [Full GC [Tenured: 9539K->2954K(56768K), 0.1853470 secs] 9994K->2954K(82368K), [Perm : 83967K->13069K(83968K)], 0.1951660 secs] [Times: user=0.19 sys=0.01, real=0.20 secs] 
   java.lang.OutOfMemoryError: PermGen space
           at java.lang.ClassLoader.defineClass(ClassLoader.java:791)
           at java.lang.ClassLoader.defineClass(ClassLoader.java:634)
           at Test.loadNext(Test.java:135)
           at Test.main(Test.java:142)
   Heap
    def new generation   total 25600K, used 911K [0x00000007bae00000, 0x00000007bc9c0000, 0x00000007d0350000)
     eden space 22784K,   3% used [0x00000007bae00000, 0x00000007baee3d60, 0x00000007bc440000)
     from space 2816K,   0% used [0x00000007bc440000, 0x00000007bc440000, 0x00000007bc700000)
     to   space 2816K,   0% used [0x00000007bc700000, 0x00000007bc700000, 0x00000007bc9c0000)
    tenured generation   total 56768K, used 2954K [0x00000007d0350000, 0x00000007d3ac0000, 0x00000007fae00000)
      the space 56768K,   5% used [0x00000007d0350000, 0x00000007d0632868, 0x00000007d0632a00, 0x00000007d3ac0000)
    compacting perm gen  total 21248K, used 13102K [0x00000007fae00000, 0x00000007fc2c0000, 0x0000000800000000)
      the space 21248K,  61% used [0x00000007fae00000, 0x00000007fbacb978, 0x00000007fbacba00, 0x00000007fc2c0000)
   
      
Reference
=========

- Oracle Technology Network > Java SE > Java Virtual Machine Specification
  Chapter 4. The class File Format
  http://docs.oracle.com/javase/specs/jvms/se7/html/jvms-4.html
