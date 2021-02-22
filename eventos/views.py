from django.shortcuts import render
from eventos.models import Eventos,Cultos,Novidades
# Create your views here.


def eventos(request):
    eventos = Eventos.objects.all()[:4]
    eventos_lista = Eventos.objects.all()
    context = {
        'eventos': eventos,
        'eventos_lista':eventos_lista
    }

    return render(request, 'eventos/events.html', context)

def evento(request,evento_id):
    evento = Eventos.objects.get(pk=evento_id)

    context = {
        'evento':evento,
    }
    return render(request, 'eventos/evento.html', context)



def cultos(request):
    cultos = Cultos.objects.all()
    context = {
        'cultos':cultos
    }
    
    return render(request, 'eventos/cultos.html', context)


def culto(request, culto_id):
    culto = Cultos.objects.get(pk=culto_id)

    context = {
        'culto':culto,
    }
    return render(request, 'eventos/culto.html', context)


def novidades(request):
    novidades = Novidades.objects.all()
    context = {
        'novidades':novidades
    }    
    return render(request, 'eventos/novidades.html',context)


def novidade(request, novidade_id):
    novidade = Novidades.objects.get(pk=novidade_id)

    context = {
        'novidade':novidade,
    }
    return render(request, 'eventos/novidade.html', context)