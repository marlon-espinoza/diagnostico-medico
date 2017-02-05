;
;	Posibles Enfermedades
;

; Gastritis
(defrule 
	gastritis (signo astenia) 
=>
	(python-call add_enfermedad 1 gastritis)
	(printout t gastritis crlf)
)

; Gastritis 2 de prueba
(defrule 
	gastritis2 (signo distencion-abdominal) (signo dispepsias)(signo dolor-abdominal)
=>
	(python-call add_enfermedad 4 gastritis4)
	(printout t gastritis4 crlf)
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
