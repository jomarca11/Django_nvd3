from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
	url(r'^home/', views.home, name='home'),
	url(r'^get_ajax_calidad_country/', views.get_ajax_calidad_country, name='get_ajax_calidad_country'),
	url(r'^get_ajax_precio_country/', views.get_ajax_precio_country, name='get_ajax_precio_country'),
	url(r'^get_ajax_precio_puntuacion/', views.get_ajax_precio_puntuacion, name='get_ajax_precio_puntuacion'),
	url(r'^get_ajax_vinos_pais/', views.get_ajax_vinos_pais, name='get_ajax_vinos_pais'),
	url(r'^get_ajax_calidad_precio/', views.get_ajax_calidad_precio, name='get_ajax_calidad_precio'),
	url(r'^get_ajax_description/', views.get_ajax_description, name='get_ajax_description'),
]
