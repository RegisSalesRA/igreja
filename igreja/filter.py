from django.core.paginator import Paginator
from django.urls import reverse_lazy
from eventos.models import Eventos
from membros.models import Jovens
from igreja.models import Igreja, Celula,Ministerio,Lideres
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

def celula_musica(request,igreja_id):
    igreja = get_object_or_404(Igreja, pk=igreja_id) 
    celulas = igreja.celula_set.all()
    celula_musica = Celula.objects.filter(ministerio='1')
    context = {
        'igreja': igreja,
        'celula_musica': celula_musica,
    }
    return render(request, 'ministerio/ministerio_musica.html' ,context)


def celula_oracao(request,igreja_id):
    igreja = get_object_or_404(Igreja, pk=igreja_id) 
    celulas = igreja.celula_set.all()
    celula_oracao = Celula.objects.filter(ministerio='2')
    context = {
        'igreja': igreja,        
        'celula_oracao': celula_oracao,
    }
    return render(request, 'ministerio/ministerio_oracao.html' ,context)

def celula_integracao(request,igreja_id):
    igreja = get_object_or_404(Igreja, pk=igreja_id) 
    celulas = igreja.celula_set.all()
    celula_integracao = Celula.objects.filter(ministerio='3')
    context = {
        'igreja': igreja,        
        'celula_integracao': celula_integracao,
    }
    return render(request, 'ministerio/ministerio_integracao.html' ,context)

def celula_estudo(request,igreja_id):
    igreja = get_object_or_404(Igreja, pk=igreja_id) 
    celulas = igreja.celula_set.all()
    celula_estudo = Celula.objects.filter(ministerio='4')
    context = {
        'igreja': igreja,
        'celula_estudo': celula_estudo,
    }
    return render(request, 'ministerio/ministerio_estudo.html' ,context)


def celula_ministerio_detail(request,igreja_id,celula_id):
    igreja = get_object_or_404(Igreja, pk=igreja_id) 
    celulas = igreja.celula_set.all()
    celula_musica = get_object_or_404(Celula, pk=celula_id)

    context = {
        'igreja': igreja,
        'celulas':celulas,
        'celula_musica': celula_musica,
    }
    return render(request, 'ministerio/ministerio_musica_detail.html' ,context)

def celula_ministerio_jovens(request,igreja_id,celula_id):
    igreja = get_object_or_404(Igreja, pk=igreja_id) 
    celulas = igreja.celula_set.all()
    celula_musica = get_object_or_404(Celula, pk=celula_id)
    jovens = celula_musica.jovens_set.all()


    context = {
        'igreja': igreja,
        'jovens': jovens,
        'celulas':celulas,
        'celula_musica': celula_musica,
    }
    return render(request, 'ministerio/ministerio_musica_detail.html' ,context)