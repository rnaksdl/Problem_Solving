#lang racket

(define (myfac n)
  (if (= n 0)
  1
  (* n (myfac (- n 1)))))

(define (addone l)
  (if (null? l)
      '()
      (let ((lfirst (car l))
            (lrest (cdr l)))
        (cons ( + lfirst 1) (addone lrest)))))