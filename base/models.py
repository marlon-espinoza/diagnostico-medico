from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Enfermedad(models.Model):
	codigo = models.CharField(max_length=30,null=True,blank=True)
	nombre = models.CharField(max_length=30)
	casusas = models.TextField(null=True,blank=True)
	tratamiento = models.TextField(null=True,blank=True)


class SignoGeneral(models.Model):
	nombre = models.CharField(max_length=150)
	explicacion = models.TextField(null=True,blank=True)

class SignoCaracteristico(models.Model):
	nombre = models.CharField(max_length=150)
	explicacion = models.TextField(null=True,blank=True)
	pregunta = models.CharField(max_length=150)

class EnfermedadSignoGeneral(models.Model):
	enfermedad = models.ForeignKey(Enfermedad)
	signo_general = models.ForeignKey(SignoGeneral)

class EnfermedadSignoCaracteristico(models.Model):
	enfermedad = models.ForeignKey(Enfermedad)
	signo_caracteristico = models.ForeignKey(SignoCaracteristico)