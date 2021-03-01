from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from rest_framework import viewsets
from membros.forms import JovemForm
from membros.models import Jovens, Ministerio
from igreja.models import Igreja
from django.shortcuts import render, get_object_or_404, redirect


def filtrocategoria(request):
    jovens = Jovens.objects.filter(nome__contains=request.GET['nome'])
    ministerios = Ministerio.objects.all()
    context = {
        'ministerios': ministerios,
        'jovens': jovens,
    }
    return render(request, 'membros/jovensfilter.html', context)


def filtroIgrejaMocidade(request):
    jovens = Igreja.objects.filter(nome__contains=request.GET['nome'])
    ministerios = Ministerio.objects.all()
    context = {
        'ministerios': ministerios,
        'jovens': jovens,
    }
    return render(request, 'membros/jovensfilter.html', context)


def categoriafiltro(request, categoria_id):
    teste = Ministerio.objects.all()
    jovensministerios = Ministerio.objects.get(id=categoria_id)
    # filtro = Ministerio.objects.filter(nome__contains=request.GET['nome'], pk=categoria_id)
    context = {
        'teste': teste,
        'jovensministerios': jovensministerios,
        # 'filtro': filtro,
    }
    return render(request, 'ministerio/ministerio.html', context)
