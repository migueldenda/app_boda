from django import forms
from django.db import models

from django.db import models

class Invitados(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)

    asistir = models.BooleanField()  
    alergia = models.BooleanField()  

    comentario = models.TextField(blank=True)
    cancion = models.TextField(blank=True)
    
    autobus = models.BooleanField()  

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"
