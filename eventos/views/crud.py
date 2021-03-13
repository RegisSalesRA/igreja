from django.shortcuts import render
from eventos.forms import EventosCreateForm,NovidadesCreateForm,CultosCreateForm
from eventos.models import Eventos,Cultos,Novidades
from django.core.paginator import Paginator
from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.core.paginator import Paginator


def dashboard_eventos(request):
    eventos = Eventos.objects.all()
    context = {
        'eventos':eventos
    }
    return render(request, 'dashboard/eventos/eventos_dashboard.html',context)


def dashboard_eventos_create(request):  
    if request.method == "POST":  
        form = EventosCreateForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('dashboard_eventos')  
            except:  
                pass  
    else:  
        form = EventosCreateForm()  
    return render(request,'dashboard/eventos/eventos_form.html',{'form':form})    


def dashboard_eventos_update(request, evento_id):  
    book = Eventos.objects.get(id=evento_id)
    form = EventosCreateForm()
    if request.method == "POST":  
        form = EventosCreateForm(request.POST, instance=book)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('dashboard_eventos')  
            except Exception as e: 
                pass    
    return render(request,'dashboard/eventos/eventos_form.html',{'form':form})  


def dashboard_eventos_delete(request, evento_id):
    eventos = Eventos.objects.get(id=evento_id)
    try:
        eventos.delete()
    except:
        pass
    return redirect('dashboard_eventos')


#

def dashboard_cultos(request):
    cultos = Cultos.objects.all()
    context = {
        'cultos':cultos
    }
    return render(request, 'dashboard/eventos/cultos_dashboard.html',context)


def dashboard_cultos_create(request):  
    if request.method == "POST":  
        form = CultosCreateForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('dashboard_cultos')  
            except:  
                pass  
    else:  
        form = CultosCreateForm()  
    return render(request,'dashboard/eventos/cultos_form.html',{'form':form})    


def dashboard_cultos_update(request, culto_id):  
    book = Cultos.objects.get(id=culto_id)
    form = CultosCreateForm()
    if request.method == "POST":  
        form = CultosCreateForm(request.POST, instance=book)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('dashboard_cultos')  
            except Exception as e: 
                pass    
    return render(request,'dashboard/eventos/cultos_form.html',{'form':form})  


def dashboard_cultos_delete(request, culto_id):
    cultos = Cultos.objects.get(id=culto_id)
    try:
        cultos.delete()
    except:
        pass
    return redirect('dashboard_cultos')



def dashboard_novidades(request):
    novidades = Novidades.objects.all()
    context = {
        'novidades':novidades
    }
    return render(request, 'dashboard/eventos/novidades_dashboard.html',context)


def dashboard_novidades_create(request):  
    if request.method == "POST":  
        form = NovidadesCreateForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('dashboard_novidades')  
            except:  
                pass  
    else:  
        form = NovidadesCreateForm()  
    return render(request,'dashboard/eventos/novidades_form.html',{'form':form})    


def dashboard_novidades_update(request, novidade_id):  
    book = Novidades.objects.get(id=novidade_id)
    form = NovidadesCreateForm()
    if request.method == "POST":  
        form = NovidadesCreateForm(request.POST, instance=book)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('dashboard_novidades')  
            except Exception as e: 
                pass    
    return render(request,'dashboard/eventos/novidades_form.html',{'form':form})  


def dashboard_novidades_delete(request, novidade_id):
    novidades = Novidades.objects.get(id=novidade_id)
    try:
        novidades.delete()
    except:
        pass
    return redirect('dashboard_novidades')