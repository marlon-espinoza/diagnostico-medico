from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from base.models import *
import clips
#from base.forms import *

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