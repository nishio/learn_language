================
 サンプルコード
================

このディレクトリは「〜」のサンプルコードを置く場所です。

細かいコード片などはCodeRunnerを使ってひとつのスクリプトにまとめて、一括で挙動をテストする仕組みになっています。
CodeRunnerの詳細はsection1にて。

section1
========

test.pyの中に2件のテストがあります。たとえば下のように書かれています。言語と、入力と、期待している出力が並んでいて、
この例では「Rubyで"""if 0〜"""のコードを実行すると、"""true!"""と出力される」と読みます。

::

   test(Ruby, """
   if 0 then
     print "true!"
   else
     print "false!"
   end
   """, """
   true!
   """)

また、test.pyの内容をReST形式で出力したものがtest.rstという名前で置かれています。Github上で見るとシンタックスハイライトなどがついて読みやすいかと思います。

https://github.com/nishio/learn_language/blob/master/book/section1/test.rst

section3
========

test.pyの中に5件のテストがあります。

- Pythonでバイトコードを観察する
- Pythonで抽象構文木を観察する
- C++で「error: '>>' should be '> >' within a nested template argument list」を起こす例


section4
========

コンパイルして眺める用
----------------------

インラインアセンブラでコメントを埋め込んだC言語のソースコードが用意されています。下記のように-Sオプションでコンパイルすることで、アセンブリ言語での記述に変換することができます。if.sという名前で出力されます。

::

   $ gcc -S if.c


筆者の環境でコンパイルしたものをif.s.txtという名前でリポジトリに入れてあります。

- if.c
- if_elseif_else.c


実行する用
----------

- if_elseif_else_goto.c: elseを使わずにgotoで実現したコード
- if_elseif_else_wo_goto.c: 素直にelseを使って実装したコード
- no_if.c: 2つのコードを両方、色々な引数で実行するコード


- while_goto.c: whileを使わずにgotoで実装したコード
- while_wo_goto.c: 素直にwhileを使って実装したコード
- no_wihle.c: 両方を試すコード


- no_for.c: for文と、for文なしで同じ内容を実装したコード


- ForLoopTest.java: Javaで3通りのfor文を試すコード

test.pyはno_if.c, no_while.c, no_for.c, ForLoopTest.javaの4つのファイルが期待通りの出力を出すかを確認します。


section5
========

- recursive.py: 再帰呼び出しのサンプルコード
- recursive.py.txt: 再帰呼び出し解説用の「作成途中のコード」
- func_call.c: 関数の呼び出しをアセンブリ言語にコンパイルして観察するためのコード(本文では使われていません)


section6
========

- exception.c: 返り値でエラーを返す例
- exception_goto.c: goto outでエラー処理をまとめる例
- exception_setjmp.c: 紙面からは割愛された、setjmp/longjmpでまとめる例
- raii: RAIIのテスト、test.pyに期待する出力が書かれています
- test.py: Python, Ruby, JSでの例外の違い
- CheckedException.java: 検査例外のサンプル

section7
========

test.py内で下記のテストをしています。

- 代入でオブジェクトはコピーされない
- Perlでのmyとlocalの挙動の違い
- Rubyでのブロック引数のスコープ
- Pythonのnonlocal宣言


section8
========

- oct.c: 0100が百ではないことを確認するコード
- int_and_float.c: intとしての足し算とfloatとしての足し算が異なる機械語であることを、アセンブリ言語にコンパイルした結果を眺めることで学ぶためのコード
- structure.c: 構造体のサンプル
- GenericsTest.java: ジェネリクスのサンプル
- generics.cpp: クラステンプレートのサンプル(ただしstructure.cからの話の流れにあわせるためclassではなくstructを使っている)
- generics.hs: 型コンストラクタのサンプル
- add_one.c: 1を加算する関数のサンプル(型推論のある言語との比較用)
- python.c: Pythonの動的型付けされた値のメモリイメージを観察するコード

test.py内では以下のテストをしています。

- 16進数と8進数の観察
- 0.3を10回足しても3.0にはならないことの確認
- x / 2で行われる演算がxの型によってことなることの観察
- Haskellでの型推論の観察
- Scalaでの型推論の観察

section9
========

test.py内では以下のテストをしています。

- 文字列をJIS, SJIS, EUC-JPで符号化してバイト列の比較
- シフト命令を追加することで「$"」が「あ」に変わることの確認
- Pythonでは非ASCIIバイトを含むファイルを実行するにはマジックコメントが必要なことの確認


