from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from igreja.forms import CelulaUpdate
from igreja.models import Igreja, Celula, Lideres,Ministerio
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from .forms import SiginUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from eventos.views import eventos
from eventos.models import Eventos,Cultos,Novidades


# Home
def home(request):
    eventos = Eventos.objects.all().order_by('data')[:5]
    cultos = Cultos.objects.all().order_by('data')[:3]
    novidades = Novidades.objects.all().order_by('created_at')[:4]

    context = {
        'eventos':eventos,
        'cultos':cultos,
        'novidades':novidades
    }

    return render(request, 'home.html',context)


# Igreja Lista

def igrejas(request):
    igrejas = Igreja.objects.all().order_by('nome')
    eventos = Eventos.objects.all().order_by('data')[:4]

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
def celulas(request, igreja_id):
    igreja = get_object_or_404(Igreja, pk=igreja_id) 
    celulas = igreja.celula_set.all()
        
    context = {
        'igreja': igreja,
        'celulas': celulas,
    }
    return render(request, 'igreja/celulas.html', context)
    

def celula(request, celula_id, igreja_id):
    igreja = Igreja.objects.get(pk=igreja_id)
    celula = igreja.celula_set.get(pk=celula_id)

    context = {
        'celula':celula,
        'igreja':igreja
    }

    return render(request, 'igreja/celula.html', context)


def jovens_celula(request, celula_id, igreja_id):
    igreja = Igreja.objects.get(pk=igreja_id)
    celula = igreja.celula_set.get(pk=celula_id)
    jovens = celula.jovens_set.all()

    context = {
        'celula':celula,
        'igreja':igreja,
        'jovens':jovens,
    }

    return render(request, 'igreja/celula_jovens.html', context)


def FormCelula(request, celula_id):
    celula = Celula.objects.get(pk=celula_id)
    form = CelulaUpdate(request.POST or None, instance=celula)

    if form.is_valid():
        form.save()
        return redirect('igrejas')
    return render(request, 'igreja/celula-form.html', {'form': form, 'celula': celula})


def deletar_celula(request):
    if request.method == 'POST' and request.is_ajax():
        celula_id = request.POST.get('celula')
        celula_delete = get_object_or_404(Celula, pk=celula_id)
        celula_delete.delete()
        return HttpResponse(status=200)
    return HttpResponse(status=500)

# Lider Lista

def lideres(request,igreja_id):
    igreja = get_object_or_404(Igreja, pk=igreja_id) 
    lideres = igreja.lideres_set.all()
    eventos = Eventos.objects.all().order_by('data')[:4]

    context = {
        'igreja': igreja,
        'lideres': lideres,
        'eventos':eventos,
    }
    return render(request, 'igreja/lideres.html',context)

def lider(request,igreja_id, lider_id):
    igreja = Igreja.objects.get(pk=igreja_id)
    lider = igreja.lideres_set.get(pk=lider_id)
    context = {
        'lider': lider,
    }
    return render(request, 'igreja/lider.html', context)

## Ministerio ##


def ministerios(request):
    ministerios = Ministerio.objects.all()
    context = {
        'ministerios': ministerios,
    }

    return render(request, context)