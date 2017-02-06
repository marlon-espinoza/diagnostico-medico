from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from base.models import *
import clips
import json
#from base.forms import *
# Clase
class Enfermedades:
	lista = {}
	def __init__ (self):
		self.lista = {}
	def add_enfermedad(self,id , codigo):
		self.lista[str(id)] = str(codigo)


# Create your views here.
class Diagnostico(TemplateView):
	template_name = 'diagnostico.html'
	def get_context_data(self, **kwargs):
		context = super(Diagnostico, self).get_context_data(**kwargs)
		signos_gen = SignoGeneral.objects.all()
		context['signos_generales'] = signos_gen
		return context

class Administrar(TemplateView):
	template_name = 'administrar_enfermedades.html'
	def get_context_data(self, **kwargs):
		context = super(Administrar, self).get_context_data(**kwargs)
		signos_gen = SignoGeneral.objects.all()
		context['signos_generales'] = signos_gen
		return context


def posiblesEnfermedades(request):
	if request.method == 'POST':
		sintomas_id = request.POST.getlist("sintomas[]")
		sintomas_id = sintomas_id[0].split(',')
		signos_car = {}
		respuesta = {}
		e = Enfermedades()
		clips.RegisterPythonFunction(e.add_enfermedad)
		clips.Load("posibles-enfermedades.clp")
		clips.Reset()
		for sintoma_id in sintomas_id:
			try:
				sintoma = SignoGeneral.objects.get(pk=sintoma_id)
				print sintoma.identificador
				clips.Assert("(signo "+sintoma.identificador+")")
			except Exception as e:
				print e
				return HttpResponse(0)

		clips.Run()
		t = clips.StdoutStream.Read()
		print t	
		print e.lista	
		# Las  preguntas se pasan por un dict que contiene como key el id de las enfermedades y en cada value
		# un arreglo con el nombre y las preguntas
		preguntas = {"1":["fibrosis","preguna 1","pregunta 2"], "2":["horror","preguna 1","pregunta 2"]}
		respuesta = {"lista":e.lista,"preguntas":preguntas}

		if len(e.lista):
			return HttpResponse(json.dumps(respuesta),content_type='application/json')
		else:
			return HttpResponse(0)

def resultadoMedico(request):
	if request.method == 'POST':
		enfermedades_id = request.POST.getlist("enfermedades[]")
		enfermedades = {}

		# for enfermedad_id in enfermedades_id:
		# 	try:
		# 		enfermedad = Enfermedad.objects.get(pk=enfermedad_id)
		# 		print enfermedad
		# 		enfermedades[enfermedad.pk]={'nombre': enfermedad.nombre, 'causas': enfermedad.casusas, 'tratamiento': enfermedad.tratamiento}
		# 	except Exception as e:
		# 		print e
		# 		return HttpResponse(0)
		enfermedades['1']={'nombre': 'Fibrosis', 'causas': 'Mucho alcohol', 'tratamiento': 'tomar agua'}

		return HttpResponse(json.dumps(enfermedades),content_type='application/json')

