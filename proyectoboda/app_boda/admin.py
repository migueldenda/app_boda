from django.contrib import admin
from .models import Invitados

@admin.register(Invitados)
class ListaInvitados(admin.ModelAdmin):
    list_display = ('nombre', 'apellidos', 'asistir', 'alergia', 'comentario', 'cancion', 'autobus')