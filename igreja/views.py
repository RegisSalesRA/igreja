from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from igreja.forms import CelulaUpdate
from igreja.models import Igreja, Celula, Lideres
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from .forms import SiginUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from eventos.views import eventos
from eventos.models import Eventos


# Home
def home(request):
    return render(request, 'home.html')


# Igreja Lista

def igrejas(request):
    igrejas = Igreja.objects.all().order_by('nome')
    eventos = Eventos.objects.all().order_by('nome')

    context = {
         'igrejas': igrejas,
         'eventos':eventos,
    }

    return render(request, 'igreja/igrejas.html', context)

def igreja(request, igreja_id):
    igreja = get_object_or_404(Igreja, pk=igreja_id)
    return render(request, 'igreja/igreja.html', {'igreja': igreja})

def deleteigreja(request, igreja_id):
    igreja = get_object_or_404(Igreja, pk=igreja_id)
    igreja.delete()
    return redirect('igrejas')


# Celula Lista
def celulas(request):
    celulas = Celula.objects.all().order_by('nome')

    context = {
        'celulas': celulas,
    }
    return render(request, 'igreja/celulas.html', context)



def celula(request, celula_id, igreja_id):
    assembleia = Igreja.objects.get(pk=igreja_id)
    celula = assembleia.celula_set.get(pk=celula_id)
    return render(request, 'igreja/celula.html', {'celula': celula})


def FormCelula(request, celula_id):
    celula = Celula.objects.get(pk=celula_id)
    form = CelulaUpdate(request.POST or None, instance=celula)

    if form.is_valid():
        form.save()
        return redirect('igrejas')
    return render(request, 'igreja/celula-form.html', {'form': form, 'celula': celula})


# Lider Lista
def lideres(request):
    lideres = Lideres.objects.all().order_by('nome')
    context = {
        'lideres': lideres
    }
    return render(request, 'igreja/lideres.html', context)




## Logins ##

def signup_view(request):
    if request.method == 'POST':
        form = SiginUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            signup_user = User.objects.get(username=username)
            # customer_group = Group.objects.get(name='Customer')
            # customer_group.user_set.add(signup_user)
    else:
        form = SiginUpForm()
    return render(request, 'login/signup.html', {'form': form})


def signin_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return redirect('signup')
    else:
        form = AuthenticationForm()
    return render(request, 'login/signin.html', {'form': form})


def signout_view(request):
    logout(request)
    return redirect('signin')