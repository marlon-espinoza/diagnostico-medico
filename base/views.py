from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.http import Http404
from base.models import *
import clips
import json, ast
#from base.forms import *
# Clase
class Enfermedades:
	lista = {}
	def __init__ (self):
		self.lista = {}
	def add_enfermedad(self,id , nombre):
		self.lista[str(id)] = str(nombre)


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

class VerEnfermedad(TemplateView):
	template_name = 'ver_enfermedad.html'
	def get_context_data(self, **kwargs):
		context = super(VerEnfermedad, self).get_context_data(**kwargs)
		idEnfermedad = kwargs.get('id')
		try:
			e = Enfermedad.objects.get(pk=idEnfermedad)
			signos_gen = EnfermedadSignoGeneral.objects.filter(enfermedad=e).order_by('-pk')
			pregs = PreguntaEnfermedad.objects.filter(enfermedad=e).order_by('pk')
			print signos_gen
			print pregs
			context['enfermedad'] = e
			context['sintomas'] = signos_gen
			context['preguntas'] = pregs
		except Exception as e:
			raise Http404
		return context


def posiblesEnfermedades(request):
	if request.method == 'POST':
		sintomas_id = request.POST.getlist("sintomas[]")
		sintomas_id = sintomas_id[0].split(',')
		signos_car = {}
		respuesta = {}
		preguntas = {}
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

		for key in e.lista:
			try:
				enfermedad = Enfermedad.objects.get(pk=key)
				p = PreguntaEnfermedad.objects.filter(enfermedad=enfermedad)
				array_preguntas = []
				array_preguntas.append(enfermedad.nombre)
				for pregunta in p:
					array_preguntas.append(pregunta.pregunta)

				preguntas[key] = array_preguntas
			except Exception as ex:
				print ex
				return HttpResponse(0)
				
		# Las  preguntas se pasan por un dict que contiene como key el id de las enfermedades y en cada value
		# un arreglo con el nombre y las preguntas

		respuesta = {"lista":e.lista,"preguntas":preguntas}

		if len(e.lista):
			return HttpResponse(json.dumps(respuesta),content_type='application/json')
		else:
			return HttpResponse(0)

def resultadoMedico(request):
	if request.method == 'POST':
		print request.POST.get("enfermedades")
		enfermedades_id = ast.literal_eval(request.POST.get("enfermedades"))
		print enfermedades_id
		enfermedades = {}

		for enfermedad_id in enfermedades_id:
			try:
				enfermedad = Enfermedad.objects.get(pk=enfermedad_id)
				print enfermedad
				enfermedades[enfermedad.pk]={'nombre': enfermedad.nombre, 'causas': enfermedad.causas, 'tratamiento': enfermedad.tratamiento}
			except Exception as e:
				print e
				return HttpResponse(0)
		# enfermedades['1']={'nombre': 'Fibrosis', 'causas': 'Mucho alcohol', 'tratamiento': 'tomar agua'}

		return HttpResponse(json.dumps(enfermedades),content_type='application/json')

def guardarEnfermedad(request):
	if request.method == 'POST':
		sintomas = []
		preguntas = []
		form = request.POST
		nombre = request.POST.get("nombre")
		codigo = request.POST.get("codigo").replace(" ","")
		causas = request.POST.get("causas")
		tratamiento = request.POST.get("tratamiento")
		sintomas = ast.literal_eval(form["sintomas"])
		print sintomas
		preguntas = ast.literal_eval(form["preguntas"])
		print preguntas
		str_asserts = ""
		clips.Load("posibles-enfermedades.clp")
		try:
			enfermedad = Enfermedad(codigo=codigo,nombre=nombre,causas=causas,tratamiento=tratamiento)
			enfermedad.save()

			for id_sintoma in sintomas:
				print id_sintoma
				sintoma = SignoGeneral.objects.get(pk=id_sintoma)
				print sintoma
				e = EnfermedadSignoGeneral(signo_general=sintoma,enfermedad=enfermedad)
				e.save()
				str_asserts+= "(signo "+sintoma.identificador+" )"
			print "aqui no se cae"
			for pregunta in preguntas:
				p = PreguntaEnfermedad(enfermedad=enfermedad,pregunta=pregunta)
				p.save()
			print "aqui no se cae"
			clips.Build("""
				(defrule """+enfermedad.codigo+" "+str_asserts+"""
				=>
				(python-call add_enfermedad """+str(enfermedad.pk)+" \""+enfermedad.nombre+"\")"+"""
				)""")
			clips.Save("posibles-enfermedades.clp")
		except Exception as e:
			print e
			enfermedad.delete()
			return HttpResponse(0)
		

		return HttpResponse(enfermedad.pk)
