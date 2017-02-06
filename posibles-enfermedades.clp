(defrule MAIN::gastritis
   (signo astenia)
   (signo somnolencia)
   =>
   (python-call add_enfermedad 6 "Gastritis"))

(defrule MAIN::hepatitis
   (signo colicosAbdominales)
   (signo fiebre)
   =>
   (python-call add_enfermedad 7 "Hepatitis"))

(defrule MAIN::colera
   (signo cinetosis)
   (signo fatiga)
   (signo disnea)
   (signo coluria)
   =>
   (python-call add_enfermedad 8 "Colera"))

