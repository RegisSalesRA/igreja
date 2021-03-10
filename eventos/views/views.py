from django.shortcuts import render
from eventos.models import Eventos,Cultos,Novidades
from django.core.paginator import Paginator


def eventos(request):
    eventos = Eventos.objects.all()[:5]
    
    eventos_lista = Eventos.objects.all()
    paginator = Paginator(eventos_lista,9)

    page = request.GET.get('p')
    eventos_lista = paginator.get_page(page)

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

    paginator = Paginator(cultos,9)

    page = request.GET.get('p')
    cultos = paginator.get_page(page)

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
    
    paginator = Paginator(novidades,9)

    page = request.GET.get('p')
    novidades = paginator.get_page(page)

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