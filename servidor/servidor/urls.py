from django.conf import settings
from django.conf.urls import include, url
from paaud import views

urlpatterns = [
    url(r'^login', views.login, name='login'),
    url(r'^datos_estudiante', views.datos_estudiante, name='datos_estudiante'),
    url(r'^datos_usuario', views.datosUsuario, name='datosUsuario'),
    url(r'^sigin', views.sigin, name='sigin'),
    url(r'^get_facultades', views.get_facultades, name='get_facultades'),
    url(r'^post_convocatoria', views.post_convocatoria, name='post_convocatoria'),
    url(r'^get_convocatorias', views.get_convocatorias, name='get_convocatorias'),
    url(r'^post_solicitud', views.post_solicitud, name='post_solicitud'),
    url(r'^get_ultimasolicitud', views.get_ultimasolicitud, name='get_ultimasolicitud'),
    url(r'^post_camponumerico', views.post_camponumerico, name='post_camponumerico'),
    url(r'^post_campobooleano', views.post_campobooleano, name='post_campobooleano'),
    url(r'^post_campostring', views.post_campostring, name='post_campostring'),
    url(r'^get_solicitudes', views.get_solicitudes, name='get_solicitudes')
]
