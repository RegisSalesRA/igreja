from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from membros.models import Jovens, Ministerio
from igreja.models import Celula, Igreja
from django.shortcuts import render, get_object_or_404, redirect


def filtrocategoria(request):
    jovens = Jovens.objects.filter(nome__contains=request.GET['nome'])
    ministerios = Ministerio.objects.all()
    context = {
        'ministerios': ministerios,
        'jovens': jovens,
    }
    return render(request, 'membros/jovensfilter.html', context)


def jovem_search(request,**kwargs):
    jovem_search = Jovens.objects.filter(nome__contains=request.GET['name'])
    
    paginator = Paginator(jovem_search,1)

    page = request.GET.get('p')
    jovem_search = paginator.get_page(page)

    context = {
        'jovem_search': jovem_search,
    }
    return render(request, 'membros/jovens_search.html', context)

def jovem_search_musica(request):
    jovem_search = Jovens.objects.filter(nome__contains=request.GET['name'])
    context = {
        'jovem_search': jovem_search,
    }
    return render(request, 'membros/jovens_search.html', context)


def filtroIgrejaMocidade(request):
    jovens = Igreja.objects.filter(nome__contains=request.GET['name'])
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

# MINISTERIOS

def jovens_ministerio_musica(request,igreja_id,celula_id):
    igreja = get_object_or_404(Igreja, pk=igreja_id) 
    celulas = igreja.celula_set.all()
    celula_musica = get_object_or_404(Celula, pk=celula_id)
    jovens = celula_musica.jovens_set.all()

    paginator = Paginator(jovens,9)

    page = request.GET.get('p')
    jovens = paginator.get_page(page)
    context = {
        'igreja': igreja,
        'jovens': jovens,
        'celulas':celulas,
        'celula_musica': celula_musica,
    }
    return render(request, 'membros/jovens_ministerio_musica.html' ,context)


def jovens_ministerio_integracao(request,igreja_id,celula_id):
    igreja = get_object_or_404(Igreja, pk=igreja_id) 
    celulas = igreja.celula_set.all()
    celula_integracao = get_object_or_404(Celula, pk=celula_id)
    jovens = celula_integracao.jovens_set.all()

    paginator = Paginator(jovens,9)

    page = request.GET.get('p')
    jovens = paginator.get_page(page)
    context = {
        'igreja': igreja,
        'jovens': jovens,
        'celulas':celulas,
        'celula_integracao': celula_integracao,
    }
    return render(request, 'membros/jovens_ministerio_integracao.html' ,context)


def jovens_ministerio_oracao(request,igreja_id,celula_id):
    igreja = get_object_or_404(Igreja, pk=igreja_id) 
    celulas = igreja.celula_set.all()
    celula_oracao = get_object_or_404(Celula, pk=celula_id)
    jovens = celula_oracao.jovens_set.all()

    paginator = Paginator(jovens,9)

    page = request.GET.get('p')
    jovens = paginator.get_page(page)

    context = {
        'igreja': igreja,
        'jovens': jovens,
        'celulas':celulas,
        'celula_oracao': celula_oracao,
    }
    return render(request, 'membros/jovens_ministerio_oracao.html' ,context)

def jovens_ministerio_estudo(request,igreja_id,celula_id):
    igreja = get_object_or_404(Igreja, pk=igreja_id) 
    celulas = igreja.celula_set.all()
    celula_estudo = get_object_or_404(Celula, pk=celula_id)
    jovens = celula_estudo.jovens_set.all()

    paginator = Paginator(jovens,9)

    page = request.GET.get('p')
    jovens = paginator.get_page(page)

    context = {
        'igreja': igreja,
        'jovens': jovens,
        'celulas':celulas,
        'celula_estudo': celula_estudo,
    }
    return render(request, 'membros/jovens_ministerio_estudo.html' ,context)        