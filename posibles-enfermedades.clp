;
;	Posibles Enfermedades
;

; Gastritis
(defrule 
	gastritis (signo distencion-abdominal) (signo dispepsias)(signo flatulencias)(signo dolor-abdominal)
=>
	(python-call add_enfermedad 1 gastritis)
	(printout t gastritis crlf)
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
	(python-call add_enfermedad 3 gastritis)
	(printout t enteritis crlf)
)
