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
	def add_enfermedad(self,cod , nombre):
		self.lista[str(cod)] = str(nombre)


# Create your views here.
class Diagnostico(TemplateView):
	template_name = 'diagnostico.html'
	def get_context_data(self, **kwargs):
		context = super(Diagnostico, self).get_context_data(**kwargs)
		signos_gen = SignoGeneral.objects.all()
		print signos_gen
		context['signos_generales'] = signos_gen
		return context

class Administrar(TemplateView):
	template_name = 'administrar_enfermedades.html'
	def get_context_data(self, **kwargs):
		context = super(Administrar, self).get_context_data(**kwargs)
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
		signos_car = {"1":["enfermedad 1","preguna 1","pregunta 2"], "2":["enfermedad 2","preguna 1","pregunta 2"]}
		respuesta = {"lista":e.lista,"signos_caracteristicos":signos_car}
		if len(e.lista):
			return HttpResponse(json.dumps(respuesta),content_type='application/json')
		else:
			return HttpResponse(0)
