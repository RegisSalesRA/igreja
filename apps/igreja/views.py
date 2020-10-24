from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from rest_framework import viewsets

from api.igreja.serializers import IgrejaSerializer, CelulaSerializer, LideresSerializer
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

# Igreja


class IgrejaView(ListView):
    model = Igreja
    template_name = 'igreja/igreja.html'
    queryset = Igreja.objects.all()
    context_object_name = 'igreja'

# Listas Cards
class ListasIgrejaView(ListView):
    model = Igreja
    template_name = 'igreja/igreja_listagem.html'
    queryset = Igreja.objects.all()
    context_object_name = 'igrejalista'


class CreateIgrejaView(CreateView):
    model = Igreja
    template_name = 'igreja/igreja_form.html'
    fields = ['endereco', 'nome_igreja', 'pastor_nome', 'descreva_igreja']
    success_url = reverse_lazy('igrejaHtml')


class UpdateIgrejaView(UpdateView):
    model = Igreja
    template_name = 'igreja/igreja_form.html'
    fields = ['endereco', 'nome_igreja', 'pastor_nome', 'descreva_igreja']
    success_url = reverse_lazy('igrejaHtml')


class DeleteIgrejaView(DeleteView):
    model = Igreja
    template_name = 'igreja/igreja_form_deletar.html'
    success_url = reverse_lazy('igrejaHtml')


# IgrejaEnd


# Lider


class LiderView(ListView):
    model = Lideres
    template_name = 'igreja/lider.html'
    queryset = Lideres.objects.all()
    context_object_name = 'lideres'


class CreateLiderView(CreateView):
    model = Lideres
    template_name = 'igreja/lider_form.html'
    fields = ['nome', 'id_igreja', 'igreja_pertence']
    success_url = reverse_lazy('liderHtml')


class UpdateLiderView(UpdateView):
    model = Lideres
    template_name = 'igreja/lider_form.html'
    fields = ['nome', 'id_igreja', 'igreja_pertence']
    success_url = reverse_lazy('liderHtml')


class DeleteLiderView(DeleteView):
    model = Lideres
    template_name = 'igreja/lider_form_deletar.html'
    success_url = reverse_lazy('liderHtml')

# LiderEnd


# Celula

class CelulaView(ListView):
    model = Celula
    template_name = 'igreja/celula.html'
    queryset = Celula.objects.all()
    context_object_name = 'celula'


class ListaCelulaView(ListView):
    model = Celula
    template_name = 'igreja/celula_listagem.html'
    queryset = Celula.objects.all()
    context_object_name = 'celulalista'


class CreateCelulaView(CreateView):
    model = Celula
    template_name = 'igreja/celula_form.html'
    fields = ['nome_celula', 'endereco', 'igreja_mae', 'lider_celula']
    success_url = reverse_lazy('celulaHtml')


class UpdateCelulaView(UpdateView):
    model = Celula
    template_name = 'igreja/celula_form.html'
    fields = ['nome_celula', 'endereco', 'igreja_mae', 'lider_celula']
    success_url = reverse_lazy('celulaHtml')


class DeleteCelulaView(DeleteView):
    model = Celula
    template_name = 'igreja/celula_form_deletar.html'
    success_url = reverse_lazy('celulaHtml')

# EndCelula


# VIEW HTML END


# HOME

def Home(request):
    return render(request, 'home.html')

