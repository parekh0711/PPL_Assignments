(defun facto (n)
  (cond
    ((= n 1) 1)
    (t (* n (facto (- n 1))))))