from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from rest_framework import viewsets
from api.membros.serializers import JovensSerializer, NovatosSerializer
from apps.membros.forms import JovemForm, NovatoForm
from apps.membros.models import Jovens, Novatos
from django.shortcuts import render, get_object_or_404, redirect


# API

class JovensView(viewsets.ModelViewSet):
    queryset = Jovens.objects.all()
    serializer_class = JovensSerializer


class NovatosView(viewsets.ModelViewSet):
    queryset = Novatos.objects.all()
    serializer_class = NovatosSerializer


# API END

# ViewHtml

def jovens(request):
    jovens = Jovens.objects.all().order_by('nome')
    return render(request, 'membros/jovens.html', {'jovens': jovens})


def jovensForm(request):
    form = JovemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('Jovens')
    return render(request, 'membros/jovem_form.html', {'form': form})


def jovenUpdate(request, jovem_id):
    jovem = Jovens.objects.get(pk=jovem_id)

    form = JovemForm(request.POST or None, instance=jovem)
    if form.is_valid():
        form.save()
        return redirect('Jovens')
    return render(request, 'membros/jovem_form.html', {'form': form, 'jovem': jovem})


def jovemDelete(request, jovem_id):
    jovem = Jovens.objects.get(pk=jovem_id)

    if request.method == 'POST':
        jovem.delete()
        return redirect('Jovens')
    return render(request, 'membros/jovem_form_deletar.html', {'jovem': jovem})



def novatos(request):
    novatos = Novatos.objects.all().order_by('nome')
    return render(request, 'membros/novato.html', {'novatos': novatos})


def novatosForm(request):
    form = NovatoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('Novatos')
    return render(request, 'membros/novato_form.html', {'form': form})


def novatoUpdate(request, novato_id):
    novato = Novatos.objects.get(pk=novato_id)

    form = NovatoForm(request.POST or None, instance=novato)
    if form.is_valid():
        form.save()
        return redirect('Novatos')
    return render(request, 'membros/novato_form.html', {'form': form, 'novato': novato})


def novatoDelete(request, novato_id):
    novato = Novatos.objects.get(pk=novato_id)

    if request.method == 'POST':
        novato.delete()
        return redirect('Novatos')
    return render(request, 'membros/novato_form_deletar.html', {'novato': novato})
