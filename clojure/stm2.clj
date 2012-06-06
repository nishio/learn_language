;
; STMの挙動を観察する2


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

; STM
(def rx (ref 0))

(with-new-thread
 (dosync
  (println "start transaction")
  (checkpoint "1")
  (ref-set rx 1)
  (println "modified ref rx: 1")
  (checkpoint "2")
  (println "finish transaction 1")
  ))

(Thread/sleep 500)
(println "----------")
(println @rx)
(Thread/sleep 500)

(open "1")

(Thread/sleep 500)
(println "----------")
(println @rx)
(Thread/sleep 500)

(open "2")

(Thread/sleep 500)
(println "----------")
(println @rx)
