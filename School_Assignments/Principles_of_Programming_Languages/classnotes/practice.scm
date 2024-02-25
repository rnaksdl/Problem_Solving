#lang scheme

; practicing

(define a 2)

(define double_it
  (lambda (x)
    (* 2 x)))

a
(double_it a)

"Hello, World" ; Sting
10             ; Integer
3.14           ; Real
'HelloWorld    ; Symbol

(sqrt (+ (* 4 4) (* 3 3)))   ; sqrt(4*4 + 3*3) = sqrt(16 + 9) = sqrt(25)

(define half_it
  (lambda (x)
    (/ x 2)))

(half_it 20)

(list 1 2 3 4)

(define kyu_bday (list 09 20 2001))
(define clr_bday '(10 09 2000))

kyu_bday
clr_bday

(append kyu_bday clr_bday)

#t
#f

(newline)

(integer? 10)

(number? (car '(8 'a 'b)))
(symbol? (cdr '(8 'a)))

(< 3 4)
(eq? 'a 'b)
(eq? 'a 'a)

(car(cdr(cdr '(a b c d))))
(caddr '(a b c d))

(cdr '(cdr '(1 2 3)))

'(())
(null? '(()))

(cons 3 '(okc dallas houston))
(cons '(3) '(okc dallas houston))
(append '(3) '(okc dallas houston))

(list 3 4 5)

(list 'dallas 'norman)

(append '(dallas) '(norman))

(cons 'dallas 'norman)

(begin (+ 3 4) (* 9 8))


(lambda (x) (+ x x))
 
((lambda (x) (+ x x)) 3)

((lambda (x y z) (y x z)) 3 + 4)
((lambda (x y z) (y x z)) 3 * 4)
((lambda (x y z) (y x z)) 3 cons '(4))

(define infix (lambda (x y z) (y x z)))
(infix '(dallas houston) append '(ada edmond))

(define (mysquare x) (* x x))
(define x 43)
(mysquare x)
