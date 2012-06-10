; スレッドを作るマクロ
; http://code.google.com/p/javaee-study/source/browse/trunk/clojure-concurrency/concurrency.clj?r=5
(import '(java.lang Thread))
(defmacro with-new-thread [& body]
  `(.start (Thread. (fn [] ~@body))))


(defn setThreadName [name] (. (Thread/currentThread) setName name))
(defn getThreadName [] (. (Thread/currentThread) getName))
; 指定された値がTrueになるまでブロックするチェックポイント
(def dict (new java.util.Hashtable))

(defn gate [key]
;  (if (not (and (.get dict key) suppress_wait_msg))
;      (println "thread" (getThreadName) "is waiting gate" key "is open"))

  (while (not (.get dict key))
    (Thread/sleep 100))

  (println "thread" (getThreadName) "passed the gate" key))


(defn open [key]
  (.put dict key true)
  (println "thread" (getThreadName) "opened gate" key ))


(defn close [key]
  (.put dict key false)
  (println "thread" (getThreadName) "closed gate" key))


(defn open-wait [key1 key2]
  (println "thread" (getThreadName) "opened gate" key1
           "and waiting until gate" key2 "is open")
  (.put dict key1 true) ; open
  (gate key2))
