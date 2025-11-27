from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('itinerario/',views.itinerario, name='itinerario'),
    path('mapa/', views.mapa, name='mapa'),
    path('pre_formulario/', views.pre_formulario, name='pre_formulario'),
    path('formulario/',views.formulario, name='formulario'),
    path('contacto/',views.contacto, name='contacto'),
]