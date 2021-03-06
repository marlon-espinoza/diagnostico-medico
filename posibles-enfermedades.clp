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

(defrule MAIN::enteritis
   (signo diarrea)
   (signo miastenia)
   (signo distensionAbdominal)
   =>
   (python-call add_enfermedad 19 "Enteritis"))

(defrule MAIN::ulcera
   (signo inapetencia)
   (signo cinetosis)
   (signo emesis)
   =>
   (python-call add_enfermedad 27 "Ulcera"))

(defrule MAIN::hepatitis
   (signo colicosAbdominales)
   (signo diarrea)
   (signo somnolencia)
   =>
   (python-call add_enfermedad 28 "Hepatitis"))

(defrule MAIN::neumonia
   (signo tosFlema)
   (signo fiebre)
   (signo escalofrio)
   (signo miaglias)
   (signo dolorArticular)
   (signo fatiga)
   (signo dolorToracico)
   =>
   (python-call add_enfermedad 29 "Neumonia"))

(defrule MAIN::tuberculosis
   (signo fatiga)
   (signo dolorToracico)
   (signo diaforesis)
   =>
   (python-call add_enfermedad 30 "Tuberculosis"))

(defrule MAIN::cancerDeEstomago
   (signo diarrea)
   (signo inapetencia)
   =>
   (python-call add_enfermedad 32 "Cancer de Estomago"))

(defrule MAIN::embolia
   (signo cefalea)
   (signo cinetosis)
   (signo espasticidad)
   (signo entumecimiento)
   =>
   (python-call add_enfermedad 33 "Embolia arterial"))

(defrule MAIN::estenosis_mitral
   (signo tosFlema)
   (signo fatiga)
   (signo infeccionesRespiratorias)
   (signo dolorToracico)
   =>
   (python-call add_enfermedad 34 "Estenosis mitral"))

(defrule MAIN::valvuloplastia_cardiaca
   (signo fatiga)
   (signo astenia)
   (signo cinetosis)
   (signo dolorToracico)
   (signo disnea)
   =>
   (python-call add_enfermedad 65 "Valvulopatía cardiaca"))

(defrule MAIN::insuficiencia_cardiaca
   (signo tosFlema)
   (signo cinetosis)
   (signo astenia)
   (signo inapetencia)
   =>
   (python-call add_enfermedad 66 "Insuficiencia cardiaca"))

