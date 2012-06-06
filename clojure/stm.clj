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
  (println "modified ref rx = 1")
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
  (println "modified ref rx = 2")
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

(comment (output checked by coderunner)
start transaction 1
thread t1 opened gate 01
start transaction 2
thread t2 closed gate 21
thread t2 opened gate 02
thread t0 passed the gate 01
thread t0 passed the gate 02
thread t0 opened gate 11 and waiting until gate 03 is open
thread t1 passed the gate 11
modified ref rx = 1
thread t1 opened gate 03
thread t0 passed the gate 03
thread t0 closed gate 02
thread t0 opened gate 21 and waiting until gate 02 is open
thread t2 passed the gate 21
transaction 2 trying to write
start transaction 2
thread t2 closed gate 21
thread t2 opened gate 02
thread t0 passed the gate 02
thread t0 closed gate 02
thread t0 opened gate 21 and waiting until gate 02 is open
thread t2 passed the gate 21
transaction 2 trying to write
start transaction 2
thread t2 closed gate 21
thread t2 opened gate 02
thread t0 passed the gate 02
thread t0 closed gate 02
thread t0 opened gate 12 and waiting until gate 04 is open
thread t1 passed the gate 12
finish transaction 1
thread t1 opened gate 04
thread t0 passed the gate 04
thread t0 opened gate 21 and waiting until gate 02 is open
thread t2 passed the gate 21
transaction 2 trying to write
start transaction 2
thread t2 closed gate 21
thread t2 opened gate 02
thread t0 passed the gate 02
thread t0 opened gate 21 and waiting until gate 02 is open
thread t0 passed the gate 02
thread t0 opened gate 22
thread t2 passed the gate 21
transaction 2 trying to write
modified ref rx = 2
thread t2 passed the gate 22
finish transaction 2
(end of comment))