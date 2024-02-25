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

(define (reduce_empty_list apoly)
  (if (or (null? apoly) (not (null? (car apoly)))) apoly
      (reduce_empty_list (cdr apoly))))

(define (lists_add_helper alist blist)
    (if (null? alist) blist
      (if (null? blist) alist
          (cons (+ (car alist) (car blist)) (lists_add_helper (cdr alist) (cdr blist))))))

(lists_add_helper '() '(0 1 2 3 0))

(define (list_add alist blist)
  (let ((result (lists_add_helper alist blist)))
    (rev_list (reduce_zero (rev_list result)))))

(list_add '() '(0 1 2 3 0))

(define (poly_add_helper apoly bpoly)
  (if (null? apoly) bpoly
      (if (null? bpoly) apoly
          (cons (list_add (car apoly) (car bpoly)) (poly_add_helper (cdr apoly) (cdr bpoly))))))

(poly_add_helper '((1 1 1)) '((2 2 2)))

(poly_add_helper '((1 1 1) () ) '((2 2 2) (1 2)))

(define (poly_add apoly bpoly)
  (let ((result (poly_add_helper apoly bpoly)))
    (rev_poly (reduce_empty_list (rev_poly result)))))

(poly_add '( (1 -1) (1 2 3) () (3)) '((-1 1) (-1 2) (3)))


(define (lists_sub_helper alist blist)
  (if (null? alist) (map - blist)
      (if (null? blist) alist
          (cons (- (car alist) (car blist)) (lists_sub_helper (cdr alist) (cdr blist))))))

(lists_sub_helper '() '(1 1 1))

(define (list_sub alist blist)
  (let ((result (lists_sub_helper alist blist)))
    (rev_list (reduce_zero (rev_list result)))))

(list_sub '(0 2 2 2 0) '(0 1 1 1 0))


(define (poly_sub_helper apoly bpoly)
  (if (null? apoly) (map (lambda (x) (map - x)) bpoly)
      (if (null? bpoly) apoly
          (cons (list_sub (car apoly) (car bpoly)) (poly_sub_helper (cdr apoly) (cdr bpoly))))))

(poly_sub_helper '(() () ()) '(() (1 1 1) ()))

(define (poly_sub apoly bpoly)
  (let ((result (poly_sub_helper apoly bpoly)))
    (rev_poly (reduce_empty_list (rev_poly result)))))

(poly_sub '(() () ()) '(() (1 1 1) ()))








(define (der_helper l1 n)
  (if (null? l1) '()
      (cons (* n (car l1)) (der_helper (cdr l1) (+ n 1)))))

(der_helper '(1 1 1 1) 0)

(define (list_derx alist)
  (let ((result (der_helper alist 0)))
    (rev_list (reduce_zero (rev_list result)))))

(list_derx '(0 0))

(define (poly_derx_helper apoly)
  (if (null? apoly) '()
      (cons (list_derx (car apoly)) (poly_derx_helper (cdr apoly)))))

(poly_derx_helper '((1) (1 2 3) ()))

(define (poly_derx apoly)
  (let ((result (poly_derx_helper apoly)))
    (rev_poly (reduce_empty_list (rev_poly result)))))

(poly_derx '( (1) (1 2 3) () (3) ()))







(define (int_list_mul_helper n alist)
  (if (null? alist) '()
      (cons (* n (car alist)) (int_list_mul_helper n (cdr alist)))))

(int_list_mul_helper 3 '(0 1 1 1 0))

(define (int_list_mul alist blist)
  (let ((result (int_list_mul_helper alist blist)))
    (rev_list (reduce_zero (rev_list result)))))

(int_list_mul 3 '(0 1 1 1 0))

(define (list_list_mul_helper alist blist)
  (if (null? alist) '()
      (if (null? blist) '()
          (list_add (int_list_mul (car alist) blist)
                    (cons 0 (list_list_mul_helper (cdr alist) blist))))))

(list_list_mul_helper '(1 1 1) '(1 1 1))

(define (list_list_mul alist blist)
  (let ((result (list_list_mul_helper alist blist)))
    (rev_list (reduce_zero (rev_list result)))))

(list_list_mul '(1 1 1) '(1 1 1))


(define (list_poly_mul_helper alist bpoly)
  (if (null? alist) '()
      (if (null? bpoly) '()
          (cons (list_list_mul alist (car bpoly)) (list_poly_mul_helper alist (cdr bpoly))))))


(define (list_poly_mul alist blist)
  (let ((result (list_poly_mul_helper alist blist)))
    (rev_poly (reduce_empty_list (rev_poly result)))))

(define (poly_poly_mul_helper apoly bpoly)
  (if (null? apoly) '()
      (if (null? bpoly) '()
          (poly_add (list_poly_mul (car apoly) bpoly) 
                    (cons '(0) (poly_poly_mul_helper (cdr apoly) bpoly))))))

(poly_poly_mul_helper '( (1) (1 2 3) () (3)) '((-1) (-1 2) (3)))

;’((-1) (-2 0 -3) (2 0 1 6) (0 6 9) (-3 6) (9))
