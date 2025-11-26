from django.shortcuts import render

def index (request):
    return render(request, 'app_boda/index.html')

def itinerario(request):
    return render(request, 'app_boda/itinerario.html')

def mapa(request):
    return render(request, 'app_boda/mapa.html')

def pre_formulario(request):
    return render(request, 'app_boda/pre_formulario.html')