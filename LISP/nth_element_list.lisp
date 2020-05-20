(defun nth2 (n lst)
  (if (zerop n)
    (car lst)
    (nth2 (1- n) (cdr lst))))