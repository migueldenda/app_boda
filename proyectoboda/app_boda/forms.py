from django import forms
from .models import Invitados

class InvitadosForm(forms.ModelForm):
    class Meta:
        model = Invitados
        fields = ['nombre', 'apellidos', 'asistir', 'alergia', 'comentario','cancion', 'autobus']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'placeholder': 'Escribe su nombre',
                'id': 'id_nombre'
            }),
            'apellidos': forms.TextInput(attrs={
                'placeholder': 'Escribe sus apellidos',
                'id': 'id_apellidos'
            }),
            'comentario': forms.Textarea(attrs={
                'placeholder': 'Cuéntanos sobre tus alergias o preferencias...',
                'id': 'id_comentario',
                'rows': 4
            }),
            'cancion': forms.Textarea(attrs={
                'placeholder': 'Una canción que no pueda faltar',
                'id': 'id_cancion',
                'rows': 4
            }),
        }

    asistir = forms.ChoiceField(
        label="¿Asistirás?",
        choices=[('True', "Sí"), ('False', "No")],
        widget=forms.RadioSelect
    )

    alergia = forms.ChoiceField(
        label="¿Tienes alergia?",
        choices=[('True', "Sí"), ('False', "No")],
        widget=forms.RadioSelect
    )

    autobus = forms.ChoiceField(
        label="¿Necesitas autobús?",
        choices=[('True', "Sí"), ('False', "No")],
        widget=forms.RadioSelect
    )