;
;	Posibles Enfermedades
;

; Gastritis
(defrule 
	enfermedad1 (signo disnea) (signo alquitranosas) 
=>
	(python-call add_enfermedad 1 fibrosis)
	(printout t fibrosis crlf)
)

; Gastritis 2 de prueba
(defrule 
	enfermedad2 (signo vomitoSangre) (signo coluria)
=>
	(python-call add_enfermedad 2 horror)
	(printout t horror crlf)
)

(defrule 
	estrenimiento (signo falta-vitalidad) (signo dificultad-defecacion)(dolor abdominal)
=>
	(python-call add_enfermedad 2 estrenimiento)
	(printout t estrenimiento crlf)
)

(defrule 
	enteritis (signo diarrea) (signo distencion-abdominal)(signo deshidratacion)(signo astenia)
=>
	(python-call add_enfermedad 3 enteritis)
	(printout t enteritis crlf)
)
