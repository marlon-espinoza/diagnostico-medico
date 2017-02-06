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

<<<<<<< HEAD
(defrule MAIN::apendicitis
   (signo colicosAbdominales)
   (signo cinetosis)
   (signo emesis)
   (signo fiebre)
   =>
   (python-call add_enfermedad 8 "Apendicitis"))

(defrule MAIN::peritonitis
   (signo escalofrio)
   (signo taquicardia)
   =>
   (python-call add_enfermedad 9 "Peritonitis"))

(defrule MAIN::colonIrritable
   (signo diarrea)
   =>
   (python-call add_enfermedad 12 "Colon Irritable"))

(defrule MAIN::gastritisAguda
   (signo alquitranosas)
   (signo vomitoSangre)
   =>
   (python-call add_enfermedad 13 "Gastritis Aguda"))

(defrule MAIN::hepatitisA
   (signo ictericia)
   (signo cinetosis)
   (signo emesis)
   (signo fiebre)
   (signo fatiga)
   =>
   (python-call add_enfermedad 14 "Hepatitis A"))

(defrule MAIN::cirrosis
   (signo ictericia)
   (signo colicosAbdominales)
   (signo inapetencia)
   =>
   (python-call add_enfermedad 15 "Cirrosis"))

(defrule MAIN::anemia
   (signo astenia)
   (signo inapetencia)
   =>
   (python-call add_enfermedad 16 "Anemia"))
=======
(defrule MAIN::colera
   (signo cinetosis)
   (signo fatiga)
   (signo disnea)
   (signo coluria)
   =>
   (python-call add_enfermedad 8 "Colera"))
>>>>>>> d325955581cd5c82ab2a793aefbc7200b86502f8

