from django import forms
from .models import Jovens

class JovemForm(forms.ModelForm):
    class Meta:
        model = Jovens
        fields = ['nome','ministerio','igreja','celula']