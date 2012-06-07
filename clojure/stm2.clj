;
; STMの挙動を観察する2
(require 'util)

; STM
(def rx (ref 0))

(setThreadName "t0")

(with-new-thread
 (setThreadName "t1")

 (dosync
  (println "**start transaction")
  (gate "1")
  (ref-set rx 1)
  (println "**modified ref rx = 1")
  (open-wait "wrote_rx" "2")
  (println "**finish transaction")
  )
 (open "end_transaction")
 )

(println "**before modification rx is" @rx)
(open-wait "1" "wrote_rx")

(println "**after modification but not end of transaction rx is" @rx)
(open-wait "2" "end_transaction")

(println "**after end of transaction rx is" @rx)


(comment (output checked by coderunner)
**start transaction
**before modification rx is 0
thread t0 opened gate 1 and waiting until gate wrote_rx is open
thread t1 passed the gate 1
**modified ref rx = 1
thread t1 opened gate wrote_rx and waiting until gate 2 is open
thread t0 passed the gate wrote_rx
**after modification but not end of transaction rx is 0
thread t0 opened gate 2 and waiting until gate end_transaction is open
thread t1 passed the gate 2
**finish transaction
thread t1 opened gate end_transaction
thread t0 passed the gate end_transaction
**after end of transaction rx is 1
(end of comment))
