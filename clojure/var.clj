;
; STMの挙動を観察する2
; varの動的スコープと静的スコープ、それがスレッドローカルであること
(require 'util)

; var
(def v 42) ; static scope
(def ^:dynamic w 42) ; dynamic scope

(defn show_v [] (println "in func, v is" v))
(defn show_w [] (println "in func, w is" w))
(setThreadName "t0")

(with-new-thread
 (setThreadName "t1")
 (let [v 142]
      (binding [w 242]
               (println "in thread1")
               (println "  v is" v)
               (show_v)
               (println "  w is" w)
               (show_w)
               (open-wait "1" "2"))))

(gate "1")
(println "in thread 0")
(println "  v is" v)
(println "  w is" w)
(open "2")

(comment (output checked by coderunner)
in thread1
  v is 142
in func, v is 42
  w is 242
in func, w is 242
thread t1 opened gate 1 and waiting until gate 2 is open
thread t0 passed the gate 1
in thread 0
  v is 42
  w is 42
thread t0 opened gate 2
thread t1 passed the gate 2
(end of comment))
