from django import forms
from membros.models import Jovens

class JovemCreateForm(forms.ModelForm):
    class Meta:
        model = Jovens
        fields = '__all__'