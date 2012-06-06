;
; STMの挙動を観察する2
; varの動的スコープと静的スコープ、それがスレッドローカルであること

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
(def v 42) ; static scope
(def ^:dynamic w 42)

(defn show_v [] (println "in func, v is" v))
(defn show_w [] (println "in func, w is" w))

(with-new-thread
 (let [v 142]
      (binding [w 242]
               (println "in thread1")
               (println "v is" v)
               (show_v)
               (println "w is" w)
               (show_w)
               (open-wait "1" "2"))))

(checkpoint "1")
(println "in thread 0")
(println "v is" v)
(println "w is" w)
(open "2")

