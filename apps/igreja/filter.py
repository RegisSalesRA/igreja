from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from rest_framework import viewsets
from api.membros.serializers import JovensSerializer, NovatosSerializer

from apps.igreja.models import Igreja
from django.shortcuts import render, get_object_or_404, redirect


def IgrejaFiltro(request):
    igrejasfiltro = Igreja.objects.filter(nome__contains=request.GET['nome'])
    paginator = Paginator(igrejasfiltro, 2)
    page_number = request.GET.get('page')
    igrejasfiltro = paginator.get_page(page_number)
    context = {
        'igrejasfiltro': igrejasfiltro,
    }
    return render(request, 'igreja/igrejas.html', context)