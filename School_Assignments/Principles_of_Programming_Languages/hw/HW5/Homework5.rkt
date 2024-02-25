#lang racket

;; Kyumin Lee, CS 3323, Homework5

;eval namespace just incase
(define-namespace-anchor a)
(define ns (namespace-anchor->namespace a))



;; small fuctions that I needed for more than one funtions

;reverses a list
(define (rev_list alist)
  (letrec ((helper (lambda (list1 list2)
                     (if (null? list1) list2
                         (helper (cdr list1) (cons (car list1) list2))))))(helper alist '())))

;reverses a list of lists
(define (rev_poly apoly)
  (letrec ((helper (lambda (poly1 poly2)
                     (if (null? poly1) poly2
                         (helper (cdr poly1) (cons (car poly1) poly2))))))(helper apoly '())))

;reduces zeros in the front of a list
(define (reduce_zero alist)
  (if (or (null? alist) (not (= 0 (car alist)))) alist
      (reduce_zero (cdr alist))))

;reduces empty lists in the front
(define (reduce_empty_list apoly)
  (if (or (null? apoly) (not (null? (car apoly)))) apoly
      (reduce_empty_list (cdr apoly))))





;;    poly_add

;adds ith element in list a to ith element in list b
(define (lists_add_helper alist blist)
    (if (null? alist) blist
      (if (null? blist) alist
          (cons (+ (car alist) (car blist)) (lists_add_helper (cdr alist) (cdr blist))))))

;takes care of zeros in the front after adding two lists
(define (list_add alist blist)
  (let ((result (lists_add_helper alist blist)))
    (rev_list (reduce_zero (rev_list result)))))

;adds two lists of lists
(define (poly_add_helper apoly bpoly)
  (if (null? apoly) bpoly
      (if (null? bpoly) apoly
          (cons (list_add (car apoly) (car bpoly)) (poly_add_helper (cdr apoly) (cdr bpoly))))))

;takes care of zeros in the front after adding two lists of lists
(define (poly_add apoly bpoly)
  (let ((result (poly_add_helper apoly bpoly)))
    (rev_poly (reduce_empty_list (rev_poly result)))))





;;    poly_sub

;subtracts ith element in list b to ith element in list a
(define (lists_sub_helper alist blist)
  (if (null? alist) (map - blist)
      (if (null? blist) alist
          (cons (- (car alist) (car blist)) (lists_sub_helper (cdr alist) (cdr blist))))))

;takes care of zeros infront after subtracting list b to list a
(define (list_sub alist blist)
  (let ((result (lists_sub_helper alist blist)))
    (rev_list (reduce_zero (rev_list result)))))

;subtracts list of lists b to list of lits a
(define (poly_sub_helper apoly bpoly)
  (if (null? apoly) (map (lambda (x) (map - x)) bpoly)
      (if (null? bpoly) apoly
          (cons (list_sub (car apoly) (car bpoly)) (poly_sub_helper (cdr apoly) (cdr bpoly))))))

;takes care of zeros infront after subtracting list of lists b to list of lists a
(define (poly_sub apoly bpoly)
  (let ((result (poly_sub_helper apoly bpoly)))
    (rev_poly (reduce_empty_list (rev_poly result)))))





;;    poly_mul

;multiplies an int to a list
(define (int_list_mul_helper n alist)
  (if (null? alist) '()
      (cons (* n (car alist)) (int_list_mul_helper n (cdr alist)))))

;takes care of zeros after int_list_mul
(define (int_list_mul alist blist)
  (let ((result (int_list_mul_helper alist blist)))
    (rev_list (reduce_zero (rev_list result)))))

;multiplies a list and a list
(define (list_list_mul_helper alist blist)
  (if (null? alist) '()
      (if (null? blist) '()
          (list_add (int_list_mul (car alist) blist)
                    (cons 0 (list_list_mul_helper (cdr alist) blist))))))

;takes care of zeros after list_list_mul
(define (list_list_mul alist blist)
  (let ((result (list_list_mul_helper alist blist)))
    (rev_list (reduce_zero (rev_list result)))))

;multiplies a list and a list of lists
(define (list_poly_mul_helper alist bpoly)
  (if (null? alist) '()
      (if (null? bpoly) '()
          (cons (list_list_mul alist (car bpoly)) (list_poly_mul_helper alist (cdr bpoly))))))

;takes care of empty lists after list_poly_mul alist blist
(define (list_poly_mul alist blist)
  (let ((result (list_poly_mul_helper alist blist)))
    (rev_poly (reduce_empty_list (rev_poly result)))))

;multiplies a list of lists and a list of lists
(define (poly_poly_mul_helper apoly bpoly)
  (if (null? apoly) '()
      (if (null? bpoly) '()
          (poly_add (list_poly_mul (car apoly) bpoly) 
                    (cons '(0) (poly_poly_mul_helper (cdr apoly) bpoly))))))

;takes care of empty lists in the front after poly_poly_mul
(define (poly_mul apoly bpoly)
  (let ((result (poly_poly_mul_helper apoly bpoly)))
    (rev_poly (reduce_empty_list (rev_poly result)))))





;;    poly_derx

;multiplies n to element in l1 and increments n each step
(define (der_helper l1 n)
  (if (null? l1) '()
      (cons (* n (car l1)) (der_helper (cdr l1) (+ n 1)))))

;retuns the derivative of the list
(define (list_derx l1)
  (if (null? l1) '()
      (if (null? (cdr l1)) '()
          (der_helper (cdr l1) 1))))

;takes derivative of list of lists
(define (poly_derx_helper apoly)
  (if (null? apoly) '()
      (cons (list_derx (car apoly)) (poly_derx_helper (cdr apoly)))))

;takes care of zeros infront after taking the derivative of a list of lists
(define (poly_derx apoly)
  (let ((result (poly_derx_helper apoly)))
    (rev_poly (reduce_empty_list (rev_poly result)))))


(poly_add '( (1 -1) (1 2 3) () (3)) '((-1 1) (-1 2) (3)))
'(() (0 4 3) (3) (3))

(poly_sub '(()) '((1 2 3)))
'((-1 -2 -3))

(poly_mul '( (1) (1 2 3) () (3)) '((-1) (-1 2) (3)))
'((-1) (-2 0 -3) (2 0 1 6) (0 6 9) (-3 6) (9))

(poly_derx '( (1) (1 2 3) () (3)))
'( () ( 2 6))

(poly_add '( (1 2) ( 3 4)) '((5 5) (6 6)) )
'((6 7) (9 10))

(poly_add '( (1 2) ( 3 492378583257342957)) '((5 5) (6 623985732935873289572395347)) )
'((6 7) (9 623985732935873289572395347))

(poly_add '( (1 2) ( 3 4)) '((5 5) (6 6 6) (7 7)) )
'((6 7) (9 10 6) (7 7))

(poly_add '( (1 2) ( 3 4 -6) (-7 -7)) '((-1 -2) (-3 6 6) (7 7)) )
'(() (0 10))

(poly_sub '( (1 2) ( 3 4)) '((5 5) (6 6)) )
'((-4 -3) (-3 -2))

(poly_sub '( (1 2 3) ( 3 4)) '((5 5) (6 6 7)) )
'((-4 -3 3) (-3 -2 -7))

(poly_derx '(( 1 2 3) (2 3 4)  (5 6)))
'((2 6) (3 8) (6))

(poly_derx '(( 1 2 3) (2 3 4 5)  (5) (6)))
'((2 6) (3 8 15))

(poly_mul '( (1 2 3) (3 4)) '((3 0 4) () () (5 0 0 6)))
'((3 6 13 8 12) (9 12 12 16) () (5 10 15 6 12 18) (15 20 0 18 24))

(poly_mul '( (1 2 -3) (3 4)) '((3 0 -4) () () (5 0 0 6)))
'((3 6 -13 -8 12) (9 12 -12 -16) () (5 10 -15 6 12 -18) (15 20 0 18 24))

(poly_add '( (1 2) ( 3 4)) '((5 5) (6 6)) )
'((6 7) (9 10))

(poly_add '( (1 2) ( 3 492378583257342957)) '((5 5) (6 623985732935873289572395347)) )
'((6 7) (9 623985732935873289572395347))

(poly_add '( (1 2) ( 3 4)) '((5 5) (6 6 6) (7 7)) )
'( (6 7)  (9 10 6) (7 7))

(poly_add '( (1 2) ( 3 4 -6) (-7 -7)) '((-1 -2) (-3 6 6) (7 7)) )
'( () (0 10))

(poly_sub '( (1 2) ( 3 4)) '((5 5) (6 6)) )
'( (-4 -3) (-3 -2))

(poly_sub '( (1 2 3) ( 3 4)) '((5 5) (6 6 7)) )
'( (-4 -3 3)   (-3 -2 -7))

(poly_derx '(( 1 2 3) (2 3 4)  (5 6)))
'( (2 6) (3 8) (6))

(poly_derx '(( 1 2 3) (2 3 4 5)  (5) (6)))
'( (2 6) (3 8 15))

(poly_mul '( (1 2 3) (3 4)) '((3 0 4) () () (5 0 0 6)))
'( (3 6 13 8 12 ) (9 12 12 16 ) ()   (5 10 15 6 12 18) (15 20 0 18 24))

(poly_mul '( (1 2 -3) (3 4)) '((3 0 -4) () () (5 0 0 6)))
'( (3 6 -13 -8 12) (9 12 -12 -16)  () (5 10 -15 6 12 -18) (15 20 0 18 24))