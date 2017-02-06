from django.conf.urls import include, url
import base.views

urlpatterns = [
   	url(r'^diagnostico/$', base.views.Diagnostico.as_view(),name="dianostico"),
   	url(r'^administrar/$', base.views.Administrar.as_view(),name="administrar"),  
   	url(r'^ver_enfermedad/(?P<id>\w+)$', base.views.VerEnfermedad.as_view(),name="ver_enfermedad"), 	
   	url(r'^posibles_enfermedades/$', base.views.posiblesEnfermedades,name="posibles_enfermedades"),   
   	url(r'^resultado_medico/$', base.views.resultadoMedico,name="resultado_medico"),   
   	url(r'^guardar_enfermedad/$', base.views.guardarEnfermedad,name="guardar_enfermedad"), 
   	]