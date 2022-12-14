from django import forms
from .models import Ticket, Registro

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['asunto', 'descripcion', 'lugar']
        widgets = {
            'asunto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '¿Que paso?'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control','placeholder' : '¿Nos das más detalles?','style':'height: 100px'}),
            'lugar': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '¿En donce se presento el incidente?'}),
        }
class RegistroForm(forms.ModelForm):
    class Meta:
        model = Registro
        fields = ['estado','comment_estado','comment_visible']
