from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator
from igreja.forms import CelulaUpdate
from igreja.models import Igreja, Celula, Lideres
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from .forms import SiginUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout


def Home(request):
    return render(request, 'home.html')


def deleteigreja(request, igreja_id):
    igreja = get_object_or_404(Igreja, pk=igreja_id)
    igreja.delete()
    return redirect('igrejas')


def Igrejas(request):
    igrejas = Igreja.objects.all().order_by('nome')
    paginator = Paginator(igrejas, 2)
    page_number = request.GET.get('page')
    igrejas = paginator.get_page(page_number)
    return render(request, 'igreja/igrejas.html', {'igrejas': igrejas})


# Listas Cards individual
def igreja(request, igreja_id):
    igreja = get_object_or_404(Igreja, pk=igreja_id)

    return render(request, 'igreja/igreja.html', {'igreja': igreja})


# Celula Lista
def Celulas(request, igreja_id):
    igreja = get_object_or_404(Igreja, pk=igreja_id)
    celulas = igreja.celula_set.all()
    paginator = Paginator(celulas, 1)
    page_number = request.GET.get('page')
    celulas = paginator.get_page(page_number)

    context = {
        'igreja': igreja,
        'celulas': celulas,
    }

    return render(request, 'igreja/celulas.html', context)


# Celula Lista
def celula(request, celula_id, igreja_id):
    assembleia = Igreja.objects.get(pk=igreja_id)
    celula = assembleia.celula_set.get(pk=celula_id)
    return render(request, 'igreja/celula.html', {'celula': celula})


# Lider Lista
def LiderLista(request, igreja_id):
    igreja = get_object_or_404(Igreja, pk=igreja_id)

    return render(request, 'igreja/lideres.html', {'igreja': igreja})


# FormCelula
def FormCelula(request, celula_id):
    celula = Celula.objects.get(pk=celula_id)
    form = CelulaUpdate(request.POST or None, instance=celula)

    if form.is_valid():
        form.save()
        return redirect('igrejas')
    return render(request, 'igreja/celula-form.html', {'form': form, 'celula': celula})


## Logins ##

def signupView(request):
    if request.method == 'POST':
        form = SiginUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            signup_user = User.objects.get(username=username)
            customer_group = Group.objects.get(name='Customer')
            customer_group.user_set.add(signup_user)
    else:
        form = SiginUpForm()
    return render(request, 'login/signup.html', {'form': form})


def signinView(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('Home')
            else:
                return redirect('signup')
    else:
        form = AuthenticationForm()
    return render(request, 'login/signin.html', {'form': form})


def signoutView(request):
    logout(request)
    return redirect('signin')