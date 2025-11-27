from django.shortcuts import redirect, render
from .forms import InvitadosForm
from django.contrib import messages
from django.urls import reverse

def index (request):
    return render(request, 'app_boda/index.html')

def itinerario(request):
    return render(request, 'app_boda/itinerario.html')

def mapa(request):
    return render(request, 'app_boda/mapa.html')

def pre_formulario(request):
    return render(request, 'app_boda/pre_formulario.html')

def formulario(request):
    if request.method == "POST":
        form = InvitadosForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Tu confirmación ha sido guardada con éxito! ¡Nos vemos pronto!')
            index_url = reverse('index') 
            
            full_redirect_url = index_url + '#message-container'
            return redirect(full_redirect_url)
        else:
            messages.error(request, '¡Error al enviar el formulario! Por favor, revisa todos los campos obligatorios.')
            return render(request, 'formulario.html', {'form': form})
    else:
        form = InvitadosForm()

    return render(request, "app_boda/formulario.html", {"form": form})

def contacto(request):
    return render(request, 'app_boda/contacto.html')