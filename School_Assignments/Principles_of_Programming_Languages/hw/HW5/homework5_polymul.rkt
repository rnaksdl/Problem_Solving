#lang racket

(define (rev_list alist)
  (letrec ((helper (lambda (list1 list2)
                     (if (null? list1) list2
                         (helper (cdr list1) (cons (car list1) list2))))))(helper alist '())))

(define (rev_poly apoly)
  (letrec ((helper (lambda (poly1 poly2)
                     (if (null? poly1) poly2
                         (helper (cdr poly1) (cons (car poly1) poly2))))))(helper apoly '())))

(define (reduce_zero alist)
  (if (or (null? alist) (not (= 0 (car alist)))) alist
      (reduce_zero (cdr alist))))

(define (lists_add_helper alist blist)
    (if (null? alist) blist
      (if (null? blist) alist
          (cons (+ (car alist) (car blist)) (lists_add_helper (cdr alist) (cdr blist))))))

(lists_add_helper '() '(0 1 2 3 0))

(define (list_add alist blist)
  (let ((result (lists_add_helper alist blist)))
    (rev_list (reduce_zero (rev_list result)))))

(list_add '() '(0 1 2 3 0))

(define (reduce_empty_list apoly)
  (if (or (null? apoly) (not (null? (car apoly)))) apoly
      (reduce_empty_list (cdr apoly))))

(reduce_empty_list '(() (1 1 1) ()))

(define (poly_add_helper apoly bpoly)
  (if (null? apoly) bpoly
      (if (null? bpoly) apoly
          (cons (list_add (car apoly) (car bpoly)) (poly_add_helper (cdr apoly) (cdr bpoly))))))

(poly_add_helper '((1 1 1)) '((2 2 2)))

(poly_add_helper '((1 1 1) () ) '((2 2 2) (1 2)))

(define (poly_add apoly bpoly)
  (let ((result (poly_add_helper apoly bpoly)))
    (rev_poly (reduce_empty_list (rev_poly result)))))
(define (int_list_mul n alist)
  (if (null? alist) '()
      (cons (* n (car alist)) (int_list_mul n (cdr alist)))))

(define (list_list_mul alist blist)
  (let loop ((a alist) (b blist) (shift 0) (result '()))
    (cond
      ((null? a) result)
      (else
       (let ((new_term (int_list_mul (car a) blist)))
         (loop (cdr a) blist (+ shift 1) (poly_add result (append (make-list shift 0) new_term))))))))

(define (list_poly_mul alist bpoly)
  (if (null? bpoly) '()
      (cons (list_list_mul alist (car bpoly)) (list_poly_mul alist (cdr bpoly)))))

(define (poly_poly_mul apoly bpoly)
  (if (null? apoly) '()
      (poly_add (list_poly_mul (car apoly) bpoly) (poly_poly_mul (cdr apoly) bpoly))))

(define (poly_mul apoly bpoly)
  (let ((result (poly_poly_mul apoly bpoly)))
    (rev_poly (reduce_empty_list (rev_poly result)))))

(poly_mul '( (1) (1 2 3) () (3)) '((-1) (-1 2) (3)))

;’((-1) (-2 0 -3) (2 0 1 6) (0 6 9) (-3 6) (9))