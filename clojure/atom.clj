;
; Atomの挙動を観察する
; 複数のAtomの変更をdosyncで囲っても、別のスレッドからは不整合な状態が見える
(require 'util)

; var
(def x (atom 0))
(def y (atom 0))
(setThreadName "t0")

(with-new-thread
 (setThreadName "t1")

 (dosync ; no meaning because x and y is not ref but atom
  (gate "1")
  (reset! x 1)
  (open-wait "2" "3")
  (reset! y 1)
  (open "4")))

; before (reset! x 1)
(println "x, y =" @x @y)

(open-wait "1" "2")

; after (reset! x 1),  before (reset! y 1)
(println "x, y =" @x @y "(inconsistent)")

(open-wait "3" "4")

; after (reset! x 1), (reset! y 1)
(println "x, y =" @x @y)

(comment (output checked by coderunner)
x, y = 0 0
thread t0 opened gate 1 and waiting until gate 2 is open
thread t1 passed the gate 1
thread t1 opened gate 2 and waiting until gate 3 is open
thread t0 passed the gate 2
x, y = 1 0 (inconsistent)
thread t0 opened gate 3 and waiting until gate 4 is open
thread t1 passed the gate 3
thread t1 opened gate 4
thread t0 passed the gate 4
x, y = 1 1
(end of comment))

