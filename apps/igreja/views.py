from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from rest_framework import viewsets

from api.igreja.serializers import IgrejaSerializer, CelulaSerializer, LideresSerializer
from apps.igreja.forms import CelulaUpdate
from apps.igreja.models import Igreja, Celula, Lideres


# API

class ViewIgreja(viewsets.ModelViewSet):
    queryset = Igreja.objects.all()
    serializer_class = IgrejaSerializer


class ViewCelula(viewsets.ModelViewSet):
    queryset = Celula.objects.all()
    serializer_class = CelulaSerializer


class ViewLideres(viewsets.ModelViewSet):
    queryset = Lideres.objects.all()
    serializer_class = LideresSerializer


# API END


# VIEW HTML

# Igreja Crud

class IgrejaView(ListView):
    model = Igreja
    template_name = 'igreja/CrudBasedViews/igreja.html'
    queryset = Igreja.objects.all()
    context_object_name = 'igreja'


class CreateIgrejaView(CreateView):
    model = Igreja
    template_name = 'igreja/CrudBasedViews/igreja_form.html'
    fields = ['nome', 'endereco', 'pastor', 'descricao']
    success_url = reverse_lazy('igrejaHtml')


class UpdateIgrejaView(UpdateView):
    model = Igreja
    template_name = 'igreja/CrudBasedViews/igreja_form.html'
    fields = ['nome', 'endereco', 'pastor', 'descricao']
    success_url = reverse_lazy('igrejaHtml')


class DeleteIgrejaView(DeleteView):
    model = Igreja
    template_name = 'igreja/CrudBasedViews/igreja_form_deletar.html'
    success_url = reverse_lazy('igrejaHtml')


# IgrejaEnd Crud


# Lider Crud


class LiderView(ListView):
    model = Lideres
    template_name = 'igreja/CrudBasedViews/lider.html'
    queryset = Lideres.objects.all()
    context_object_name = 'lideres'


class CreateLiderView(CreateView):
    model = Lideres
    template_name = 'igreja/CrudBasedViews/lider_form.html'
    fields = ['nome', 'codigo_igreja', 'igreja']
    success_url = reverse_lazy('liderHtml')


class UpdateLiderView(UpdateView):
    model = Lideres
    template_name = 'igreja/CrudBasedViews/lider_form.html'
    fields = ['nome', 'codigo_igreja', 'igreja']
    success_url = reverse_lazy('liderHtml')


class DeleteLiderView(DeleteView):
    model = Lideres
    template_name = 'igreja/CrudBasedViews/lider_form_deletar.html'
    success_url = reverse_lazy('liderHtml')


# LiderEnd Crud


# Celula Crud

class CelulaView(ListView):
    model = Celula
    template_name = 'igreja/CrudBasedViews/celula.html'
    queryset = Celula.objects.all()
    context_object_name = 'celula'


# List Celulas
class ListaCelulaView(ListView):
    model = Celula
    template_name = 'igreja/celulas.html'
    queryset = Celula.objects.all()
    context_object_name = 'celulalista'


class CreateCelulaView(CreateView):
    model = Celula
    template_name = 'igreja/CrudBasedViews/celula_form.html'
    fields = ['nome_celula', 'endereco', 'igreja_mae', 'lider_celula']
    success_url = reverse_lazy('celulaHtml')


class UpdateCelulaView(UpdateView):
    model = Celula
    template_name = 'igreja/CrudBasedViews/celula_form.html'
    fields = ['nome_celula', 'endereco', 'igreja_mae', 'lider_celula']
    success_url = reverse_lazy('celulaHtml')


class DeleteCelulaView(DeleteView):
    model = Celula
    template_name = 'igreja/CrudBasedViews/celula_form_deletar.html'
    success_url = reverse_lazy('celulaHtml')


# EndCelula Crud

# VIEW HTML END


# HOME
def Home(request):
    return render(request, 'home.html')


# Home End

##########################################################
# Listas Cards
def Igrejas(request):
    igrejas = Igreja.objects.all().order_by('nome')
    # context = {
    #     'igrejas': igrejas,
    # }
    return render(request, 'igreja/igrejas.html', {'igrejas': igrejas})


# Listas Cards individual
def igreja(request, igreja_id):
    igreja = get_object_or_404(Igreja, pk=igreja_id)

    return render(request, 'igreja/igreja.html', {'igreja': igreja})


# Celula Lista
def Celulas(request, igreja_id):
    igreja = get_object_or_404(Igreja, pk=igreja_id)
    context = {
        'igreja': igreja,
        # 'celula': celula,
    }

    return render(request, 'igreja/celulas.html', context)


# Celula Lista
def celula(request, celula_id, igreja_id):
    assembleia = Igreja.objects.get(pk=igreja_id)
    celula = assembleia.celula_set.get(pk=celula_id)
    return render(request, 'igreja/celula.html', {'celula': celula})


# Lider Lista
def LiderLista(request, igreja_id):
    igreja = get_object_or_404(Igreja, pk=igreja_id)

    return render(request, 'igreja/lideres.html', {'igreja': igreja})


# FormCelula
def FormCelula(request,celula_id):
    celula = Celula.objects.get(pk=celula_id)
    form = CelulaUpdate(request.POST or None, instance=celula)

    if form.is_valid():
        form.save()
        return redirect('igrejas')
    return render(request, 'igreja/celula-form.html', {'form': form, 'celula': celula})