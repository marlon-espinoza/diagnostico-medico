from __future__ import unicode_literals

from django.db import models

# Create your models here.
class TipoEnfermedad(models.Model):
	nombre = models.CharField(max_length=30)

	def __unicode__(self):
		return self.nombre


class Enfermedad(models.Model):
	codigo = models.CharField(max_length=30,null=True,blank=True)
	nombre = models.CharField(max_length=30)
	causas = models.TextField(null=True,blank=True)
	tratamiento = models.TextField(null=True,blank=True)
	tipo_enfermedad = models.ForeignKey(TipoEnfermedad,null=True)

	def __unicode__(self):
		return self.nombre


class SignoGeneral(models.Model):
	identificador = models.CharField(max_length=30,unique=True)
	nombre = models.CharField(max_length=150)
	explicacion = models.TextField(null=True,blank=True)

	def __unicode__(self):
		return self.nombre

# Preguntas de signos caracteristicos de una enfermedad
class PreguntaEnfermedad(models.Model):
	enfermedad = models.ForeignKey(Enfermedad)
	pregunta = models.CharField(max_length=400)

	def __unicode__(self):
		return self.enfermedad.nombre

class EnfermedadSignoGeneral(models.Model):
	enfermedad = models.ForeignKey(Enfermedad)
	signo_general = models.ForeignKey(SignoGeneral)

	def __unicode__(self):
		return self.enfermedad.nombre + " - " + self.signo_general.nombre
