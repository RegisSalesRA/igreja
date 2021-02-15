from django.shortcuts import render
from eventos.models import Eventos,Cultos,Novidades
# Create your views here.


def eventos(request):
    eventos = Cultos.objects.all()
    context = {
        'eventos': eventos,
    }

    return render(request, 'eventos.html', context)