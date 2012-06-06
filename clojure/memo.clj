; グローバルに書き換え可能な値を作る
(def dict (new java.util.Hashtable))
(.put dict "x" true)
(.get dict "x")

; sleep
(Thread/sleep 1000)

; while文
(while truth-expression
  (call-some-function))


; スレッドを作ってみる(xを監視してtrueの間ループ)
(with-new-thread
 (while (.get dict "x")
   (println "running")
   (Thread/sleep 1000)))

; 他のスレッドからxを書き換えてスレッドを止める
(.put dict "x" false)




; グローバルに書き換え可能な値を作る
(def dict (new java.util.Hashtable))

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
  (.put dict key true))

; STM
(def rx (ref 0))

(with-new-thread
 (dosync
  (println "start transaction 1")
  (checkpoint "11") ; block
  (ref-set rx 1)
  (println "modified ref rx: 1")
  (checkpoint "12") ; block
  (println "finish transaction 1")
  ))

(with-new-thread
 (dosync
  (println "start transaction 2")
  (checkpoint "21") ; block
  (ref-set rx 2)
  (println "modified ref rx: 2")
  (checkpoint "22") ; block
  (println "finish transaction 2")
  ))



(defn puts [msg] (. System/out println msg))

user=> (defmacro foo [& args] `(1 2 ~@args 3 4))
#'user/foo
user=> (macroexpand '(foo 9 9 9))
(1 2 9 9 9 3 4)
