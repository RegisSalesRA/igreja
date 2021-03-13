from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from igreja.forms import CelulaUpdate, LideresCreateForm, MinisterioCreateForm
from igreja.models import Igreja, Celula, Lideres,Ministerio
from igreja.forms import IgrejaCreateForm,CelulaCreateForm


def dashboard_igrejas(request):
    igrejas = Igreja.objects.all()
    context = {
        'igrejas':igrejas
    }
    return render(request, 'dashboard/igreja/igrejas_dashboard.html',context)

 
def dashboard_igrejas_create(request):  
    if request.method == "POST":  
        form = IgrejaCreateForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('dashboard_igrejas')  
            except:  
                pass  
    else:  
        form = IgrejaCreateForm()  
    return render(request,'dashboard/igreja/igrejas_form.html',{'form':form})    


def dashboard_igrejas_update(request, igreja_id):  
    book = Igreja.objects.get(id=igreja_id)
    form = IgrejaCreateForm()
    if request.method == "POST":  
        form = IgrejaCreateForm(request.POST, instance=book)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('dashboard_igrejas')  
            except Exception as e: 
                pass    
    return render(request,'dashboard/igreja/igrejas_form.html',{'form':form})  


def dashboard_igrejas_delete(request, igreja_id):
    igreja = Igreja.objects.get(id=igreja_id)
    try:
        igreja.delete()
    except:
        pass
    return redirect('dashboard_igrejas')    


def dashboard_celulas(request):
    celulas = Celula.objects.all()
    context = {
        'celulas':celulas
    }
    return render(request, 'dashboard/igreja/celulas_dashboard.html',context)

 
def dashboard_celulas_create(request):  
    if request.method == "POST":  
        form = CelulaCreateForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('dashboard_celulas')  
            except:  
                pass  
    else:  
        form = CelulaCreateForm()  
    return render(request,'dashboard/igreja/celulas_form.html',{'form':form})    


def dashboard_celulas_update(request, celula_id):  
    book = Celula.objects.get(id=celula_id)
    form = CelulaCreateForm()
    if request.method == "POST":  
        form = CelulaCreateForm(request.POST, instance=book)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('dashboard_celulas')  
            except Exception as e: 
                pass    
    return render(request,'dashboard/igreja/celulas_form.html',{'form':form})  


def dashboard_celulas_delete(request, celula_id):
    celula = Celula.objects.get(id=celula_id)
    try:
        celula.delete()
    except:
        pass
    return redirect('dashboard_celulas')



def dashboard_lideres(request):
    lideres = Lideres.objects.all()
    context = {
        'lideres':lideres
    }
    return render(request, 'dashboard/igreja/lideres_dashboard.html',context)


def dashboard_lideres_create(request):  
    if request.method == "POST":  
        form = LideresCreateForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('dashboard_lideres')  
            except:  
                pass  
    else:  
        form = LideresCreateForm()  
    return render(request,'dashboard/igreja/lideres_form.html',{'form':form})    


def dashboard_lideres_update(request, lider_id):  
    book = Lideres.objects.get(id=lider_id)
    form = LideresCreateForm()
    if request.method == "POST":  
        form = LideresCreateForm(request.POST, instance=book)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('dashboard_lideres')  
            except Exception as e: 
                pass    
    return render(request,'dashboard/igreja/lideres_form.html',{'form':form})  


def dashboard_lideres_delete(request, lider_id):
    lider = Lideres.objects.get(id=lider_id)
    try:
        lider.delete()
    except:
        pass
    return redirect('dashboard_lideres')


def dashboard_ministerios(request):
    ministerios = Ministerio.objects.all()
    context = {
        'ministerios':ministerios
    }
    return render(request, 'dashboard/igreja/ministerio_dashboard.html',context)


def dashboard_ministerios_create(request):  
    if request.method == "POST":  
        form = MinisterioCreateForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('dashboard_ministerios')  
            except:  
                pass  
    else:  
        form = MinisterioCreateForm()  
    return render(request,'dashboard/igreja/ministerios_form.html',{'form':form})    


def dashboard_ministerios_update(request, ministerio_id):  
    book = Ministerio.objects.get(id=ministerio_id)
    form = MinisterioCreateForm()
    if request.method == "POST":  
        form = MinisterioCreateForm(request.POST, instance=book)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('dashboard_ministerios')  
            except Exception as e: 
                pass    
    return render(request,'dashboard/igreja/ministerios_form.html',{'form':form})  


def dashboard_ministerios_delete(request, ministerio_id):
    ministerio = Ministerio.objects.get(id=ministerio_id)
    try:
        ministerio.delete()
    except:
        pass
    return redirect('dashboard_ministerios')