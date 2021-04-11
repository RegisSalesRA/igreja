from django import forms
from .models import Celula,Igreja,Lideres,Ministerio
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class IgrejaCreateForm(forms.ModelForm):
    class Meta:
        model = Igreja
        fields = '__all__'

class CelulaCreateForm(forms.ModelForm):
    class Meta:
        model = Celula
        fields = '__all__'

class LideresCreateForm(forms.ModelForm):
    class Meta:
        model = Lideres
        fields = '__all__'

class MinisterioCreateForm(forms.ModelForm):
    class Meta:
        model = Lideres
        fields = '__all__'


class MinisterioCreateForm(forms.ModelForm):
    class Meta:
        model = Ministerio
        fields = '__all__'

class CelulaUpdate(forms.ModelForm):
    class Meta:
        model = Celula
        fields = ['nome', 'endereco', 'igreja']


class SiginUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(max_length=250, help_text='eg. youremail@gmail.com')

    
    
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']
