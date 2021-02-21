from django.core.paginator import Paginator
from django.urls import reverse_lazy
from rest_framework import viewsets
from eventos.models import Eventos
from igreja.models import Igreja
from django.shortcuts import render, get_object_or_404, redirect


def igreja_search(request):
    igreja_search = Igreja.objects.filter(nome__contains=request.GET['name'])
    eventos = Eventos.objects.all().order_by('data')[:4]
    # paginator = Paginator(igreja_search, 2)
    # page_number = request.GET.get('page')
    # igreja_search = paginator.get_page(page_number)
    context = {
        'igreja_search': igreja_search,
        'eventos':eventos,
    }
    return render(request, 'igreja/igreja_search.html', context)