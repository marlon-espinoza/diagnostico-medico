from django.conf.urls import include, url
import base.views

urlpatterns = [
   	url(r'^diagnostico/$', base.views.Diagnostico.as_view(),name="dianostico"),
   	url(r'^administrar/$', base.views.Administrar.as_view(),name="administrar"),   	
   	]