from eventos.models import Eventos
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from membros.models import Jovens, Ministerio
from igreja.models import Igreja
from django.shortcuts import render, get_object_or_404, redirect



def jovens(request):
    jovens = Jovens.objects.all().order_by('nome')
    ministerios = Ministerio.objects.all()
    eventos = Eventos.objects.all().order_by('data')[:4]

    paginator = Paginator(jovens,9)

    page = request.GET.get('p')
    jovens = paginator.get_page(page)

    context = {
        'ministerios': ministerios,
        'jovens': jovens,
        'eventos':eventos,
    }
    return render(request, 'membros/jovens.html', context)

def jovem(request, jovem_id):
    jovem = get_object_or_404(Jovens, pk=jovem_id)

    context = {
        'jovem':jovem,
    }

    return render(request, 'membros/jovem.html', context)


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



from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from membros.api.serializers import JovensSerializer
from membros.models import Jovens
# Create your views here.

class JovensView(viewsets.ModelViewSet):
    queryset = Jovens.objects.all()
    serializer_class = JovensSerializer
