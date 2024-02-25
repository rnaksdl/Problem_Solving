#lang racket

(define lazycube
    (letrec ((next (lambda (n)
                     (cons (* (* n n) n) (delay (next (+ n 1)))))))
        (next 1)))
