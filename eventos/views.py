from django.shortcuts import render
from eventos.models import Eventos,Cultos,Novidades
# Create your views here.


def eventos(request):
    eventos = Eventos.objects.all()
    context = {
        'eventos': eventos,
    }

    return render(request, 'eventos/events.html', context)


def cultos(request):
    cultos = Cultos.objects.all()
    context = {
        'cultos':cultos
    }
    
    return render(request, 'eventos/cultos.html', context)