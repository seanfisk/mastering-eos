;;; Directory Local Variables
;;; See Info node `(emacs) Directory Variables' for more information.

((latex-mode
  (TeX-master . "mastering-eos")
  (eval . (add-to-list
           'TeX-style-path
           (expand-file-name
            "style"
            (file-name-directory
             (let ((d (dir-locals-find-file ".")))
               (if (stringp d) d (car d)))))))))
