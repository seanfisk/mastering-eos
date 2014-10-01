;;; Directory Local Variables
;;; See Info node `(emacs) Directory Variables' for more information.

;; Adapted from http://stackoverflow.com/a/11474657

((latex-mode
   (TeX-master . "mastering-eos")
   (eval . (add-to-list
             'TeX-style-path
             (expand-file-name
               "style"
               (let ((d (dir-locals-find-file ".")))
                 (if (stringp d)
                   ;; dir-locals-find-file can return a string, which
                   ;; will be the path to the .dir-locals.el file.
                   (file-name-directory d)
                   ;; dir-locals-find-file can also return a list, in
                   ;; which case the first element will be the directory
                   ;; containing the .dir-locals.el file.
                   (car d))))))))
