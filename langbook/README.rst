============================================
 「コーディングを支える技術」サンプルコード
============================================

このディレクトリは拙著「コーディングを支える技術」のサンプルコードなどを置く場所です。

「コーディングを支える技術」についての詳細はこちら: http://nhiro.org/langbook/

挙動の確認を手軽にするために、細かいコード片はCodeRunnerを使ってひとつのスクリプト(test.py)にまとめています。

CodeRunnerについての詳細はこちら(詳細を知らなくても以下のサンプルを読む上での支障はありません): https://github.com/nishio/learn_language/tree/master/coderunner


section1
========

test.pyの中に2件のテストが書かれています。下のように、言語と、入力と、期待している出力が並んでいます。
この例では「Rubyで ``if 0 then〜end`` のコードを実行すると、 ``true!`` と出力される」と読みます。

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

また、test.pyの内容をReST形式で出力したものが各章ごとにREADME.rstという名前で置かれています。Github上で見るとシンタックスハイライトがついて読みやすいかと思います。

https://github.com/nishio/learn_language/blob/master/book/section1/README.rst

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

elseについて
~~~~~~~~~~~~

- if_elseif_else_goto.c: elseを使わずにgotoで実現したコード
- if_elseif_else_wo_goto.c: 素直にelseを使って実装したコード
- no_if.c: 2つのコードを両方、色々な引数で実行するコード


whileについて
~~~~~~~~~~~~~

- while_goto.c: whileを使わずにgotoで実装したコード
- while_wo_goto.c: 素直にwhileを使って実装したコード
- no_wihle.c: 両方を試すコード


forについて
~~~~~~~~~~~

- no_for.c: for文と、for文なしで同じ内容を実装したコード
- ForLoopTest.java: Javaで3通りのfor文を試すコード

test.pyはno_if.c, no_while.c, no_for.c, ForLoopTest.javaの4つのファイルが期待通りの出力を出すかを確認します。


section5
========

- recursive.py: 再帰呼び出しのサンプルコード
- recursive.py.txt: 再帰呼び出し解説用の「作成途中のコード」
- func_call.c: 関数の呼び出しをアセンブリ言語にコンパイルして観察するためのコード(紙面からは割愛されました)


section6
========

- exception.c: 返り値でエラーを返す例
- exception_goto.c: goto outでエラー処理をまとめる例
- exception_setjmp.c: setjmp/longjmpでまとめる例(紙面からは割愛されました)
- raii: RAIIのテスト、test.pyに期待する出力が書かれています
- smalldisk: C言語でディスク容量不足でwriteが失敗した時に-1が返ってくることを確認する例(紙面からは割愛されました)
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

section10
=========

IgnoreLock.java
---------------

きちんとロックを確認せずにアクセスするメソッド(synchronizeをつけていないメソッド)があった場合に何が起こるかの検証用です。(紙面からは割愛されました)

consistency_checkメソッドはメソッドの冒頭と末尾でvalueの値が変わっていないかどうかをチェックします。
consistency_checkメソッドにはsynchronizedがついています。正しく同期化されていれば実行中にvalueの値が変わることはないはずです。
しかしsynchronizedのついていないignore_lockメソッドがロックを無視してvalueを書き換えます。
その結果「consistency check finished: false」というメッセージが時々表示されます。

この現象はignore_lockにsynchronizeを付ければ起こらなくなります。みなさんの手元で確認してみましょう。

section11
=========

test.py内では以下のテストをしています。

- C言語でstaticを使って「状態を持つ関数」を作るサンプル(紙面からは割愛されました)
- Perlのパッケージでカウンタを作る
- Perlで、ハッシュを値の保存場所として使う
- Perlで、ハッシュの作成などの初期化の処理自体をパッケージに入れる
- Perlで、パッケージとハッシュを結びつける(bless)
- Perlで、blessの処理を初期化時に行う
- JSで、ハッシュに関数を入れる
- JSで、複数のハッシュ内の関数が異なるインスタンスであることの確認
- JSで、プロトタイプの挙動を確認
- JSで、プロトタイプに関数をもたせる

section12
=========

test.py内では以下のテストをしています。

- TestMultiImpl.java: extendsではなくimplementsを使うことで、複数のクラスからの「仕様の継承」ができることの確認
- TestMultiImpl2.java: TestMultiImpl.javaからhello()の実装を取り除いたもの。持っているべきメソッドを持っていないために、コンパイル時にエラーになる。
- TestMultiImpl3.java: 複数のクラスをextendsしようとすると、文法エラーになる。extendsは後ろにただ1つのクラス名を取る文法になっているため。
- TestDelegate.java: 継承によって他のクラスのメソッドを自分のメソッドにする方法と、委譲によって他のオブジェクトが持つメソッドを呼び出して利用する方法の比較

- Pythonで、継承の挙動の確認
- Pythonで、複数の親クラスが同名のメンバを持っている場合に左親が優先されることを確認
- Pythonで、親クラスと子クラスで同名のメンバを持っている場合に、子クラスの値が使われること（オーバーライド）を確認
- Pythonで、上記二つのルールの影響で、菱型継承時に子クラスがオーバーライドしたメンバを親クラスの値が上書きしてしまう現象を確認
- Pythonのnew-style classで、上記問題点が解決されたことの確認

- Rubyで、moduleを使った多重継承（Mix-in）の挙動を確認
- RubyのMix-inではincludeの順番によって挙動が変わることを確認

