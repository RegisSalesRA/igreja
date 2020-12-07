from django import forms
from .models import Celula

class CelulaUpdate(forms.ModelForm):
    class Meta:
        model = Celula
        fields = ['nome','endereco','igreja']