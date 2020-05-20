(setf fact 1)
(defun facto(n)
    ( loop for x from 2 to n
           do(setq fact (* x fact))
           )
    (print fact)
    )