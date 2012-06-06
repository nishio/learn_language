;
; STMの挙動を観察する
(require 'util)

; STM
(def rx (ref 0))

(setThreadName "t0")


(with-new-thread
 (setThreadName "t1")

 (dosync
  (println "start transaction 1")
  (open "01")
  (gate "11")
  (ref-set rx 1)
  (println "modified ref rx: 1")
  (open "03")
  (gate "12")
  (println "finish transaction 1")
  (open "04")
  ))

(with-new-thread
 (setThreadName "t2")

 (dosync
  (println "start transaction 2")
  (close "21")
  (open "02")
  (gate "21")
  (println "transaction 2 trying to write")
  (ref-set rx 2)
  (println "modified ref rx: 2")
  (gate "22")
  (println "finish transaction 2")
  ))

(gate "01")
(gate "02")

(open-wait "11" "03")

(close "02")

(open-wait "21" "02")

(close "02")

(open-wait "21" "02")

(close "02")
(open-wait "12" "04")

(open-wait "21" "02")

(open-wait "21" "02")

(open "22")

