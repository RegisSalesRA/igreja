from eventos.models import Eventos
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from rest_framework import viewsets
from membros.forms import JovemForm
from membros.models import Jovens, Ministerio
from igreja.models import Igreja
from django.shortcuts import render, get_object_or_404, redirect


def mocidade(request):
    igrejas = Igreja.objects.all()
    ministerios = Ministerio.objects.all()
    context = {
        'ministerios': ministerios,
        'igrejas': igrejas,
    }

    return render(request, 'membros/igrejamocidade.html', context)

def mocidadelista(request,igreja_id):
    searchjoven = Jovens.objects.filter()
    ministerioss = Ministerio.objects.all()
    igreja = Igreja.objects.get(pk=igreja_id)
    context = {'igrejas':igreja, 'ministerioss':ministerioss, 'searchjoven':searchjoven}
    return render(request, 'membros/mocidadelista.html', context)


def jovens(request):
    jovens = Jovens.objects.all().order_by('nome')
    ministerios = Ministerio.objects.all()
    eventos = Eventos.objects.all().order_by('data')[:4]
    context = {
        'ministerios': ministerios,
        'jovens': jovens,
        'eventos':eventos,
    }
    return render(request, 'membros/jovens.html', context)


def jovensForm(request):
    form = JovemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('jovens')
    return render(request, 'membros/jovem_form.html', {'form': form})


def jovenUpdate(request, jovem_id):
    jovem = Jovens.objects.get(pk=jovem_id)

    form = JovemForm(request.POST or None, instance=jovem)
    if form.is_valid():
        form.save()
        return redirect('jovens')
    return render(request, 'membros/jovem_form.html', {'form': form, 'jovem': jovem})


def jovemDelete(request, jovem_id):
    jovem = Jovens.objects.get(pk=jovem_id)

    if request.method == 'POST':
        jovem.delete()
        return redirect('jovens')
    return render(request, 'membros/jovem_form_deletar.html', {'jovem': jovem})


def novatos(request):
    novatos = Novatos.objects.all().order_by('nome')
    return render(request, 'membros/novato.html', {'novatos': novatos})


def novatosForm(request):
    form = NovatoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('novatos')
    return render(request, 'membros/novato_form.html', {'form': form})


def novatoUpdate(request, novato_id):
    novato = Novatos.objects.get(pk=novato_id)

    form = NovatoForm(request.POST or None, instance=novato)
    if form.is_valid():
        form.save()
        return redirect('novatos')
    return render(request, 'membros/novato_form.html', {'form': form, 'novato': novato})


def novatoDelete(request, novato_id):
    novato = Novatos.objects.get(pk=novato_id)

    if request.method == 'POST':
        novato.delete()
        return redirect('novatos')
    return render(request, 'membros/novato_form_deletar.html', {'novato': novato})
