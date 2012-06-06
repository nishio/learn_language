;
; Atomの挙動を観察する
; 複数のAtomの変更をdosyncで囲っても、別のスレッドからは不整合な状態が見える

; スレッドを作るマクロ
; http://code.google.com/p/javaee-study/source/browse/trunk/clojure-concurrency/concurrency.clj?r=5
(import '(java.lang Thread))
(defmacro with-new-thread [& body]
  `(.start (Thread. (fn [] ~@body))))

; 指定された値がTrueになるまでブロックするチェックポイント
(def dict (new java.util.Hashtable))

(defn checkpoint [key]
  (while (not (.get dict key))
    (Thread/sleep 100)))

(defn open [key]
  (.put dict key true)
  (println "open" key))

(defn open-wait [key1 key2]
  (println "open gate" key1 "and wait until gate" key2 "open")
  (open key1)
  (checkpoint key2))

; var
(def x (atom 0))
(def y (atom 0))

(with-new-thread
 (dosync ; no meaning because x and y is not ref but atom
  (checkpoint "1")
  (reset! x 1)
  (open "2")

  (checkpoint "3")
  (reset! y 1)
  (open "4")))

; before (reset! x 1)
(println "x, y =" @x @y)

(open "1")
(checkpoint "2")

; after (reset! x 1),  before (reset! y 1)
(println "x, y =" @x @y)

(open "3")
(checkpoint "4")

; after (reset! x 1), (reset! y 1)
(println "x, y =" @x @y)

;output -----
x, y = 0 0
open 1
open 2
x, y = 1 0
open 3
open 4
x, y = 1 1

