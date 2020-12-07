from django import forms
from .models import Jovens,Novatos

class JovemForm(forms.ModelForm):
    class Meta:
        model = Jovens
        fields = ['nome','ministerio','igreja','celula']

class NovatoForm(forms.ModelForm):
    class Meta:
        model = Novatos
        fields = ['nome']