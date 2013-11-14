(TeX-add-style-hook
 "minted"
 (lambda ()
   (message "ran minted")
   (add-to-list 'LaTeX-verbatim-macros-with-delims-local "bash")
   (add-to-list 'LaTeX-verbatim-environments-local "bashcode")
   (when (and (featurep 'font-latex)
              (eq TeX-install-font-lock 'font-latex-setup))
     (font-latex-set-syntactic-keywords)
     (setq font-lock-set-defaults nil)
     (font-lock-set-defaults))))
