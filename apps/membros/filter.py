from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from rest_framework import viewsets
from api.membros.serializers import JovensSerializer, NovatosSerializer
from apps.membros.forms import JovemForm, NovatoForm
from apps.membros.models import Jovens, Novatos, Ministerio
from apps.igreja.models import Igreja
from django.shortcuts import render, get_object_or_404, redirect


def filtrocategoria(request):
    jovens = Jovens.objects.filter(nome__contains=request.GET['nome'])
    ministerios = Ministerio.objects.all()
    context = {
        'ministerios': ministerios,
        'jovens': jovens,
    }
    return render(request, 'membros/jovensfilter.html', context)


def categoriafiltro(request,categoria_id):
    ministerios = Ministerio.objects.get(id=categoria_id)
    return render(request, 'ministerio/ministerio.html', {'ministerio':ministerios})
