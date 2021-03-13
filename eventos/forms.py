from django import forms
from .models import Eventos,Novidades,Cultos

class EventosCreateForm(forms.ModelForm):
    class Meta:
        model = Eventos
        fields = '__all__'

class NovidadesCreateForm(forms.ModelForm):
    class Meta:
        model = Novidades
        fields = '__all__'

class CultosCreateForm(forms.ModelForm):
    class Meta:
        model = Cultos
        fields = '__all__'
