from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from igreja.forms import CelulaUpdate
from igreja.models import Igreja, Celula, Lideres,Ministerio
from igreja.forms import IgrejaCreateForm

def dashboard_igrejas(request):
    igrejas = Igreja.objects.all()
    context = {
        'igrejas':igrejas
    }
    return render(request, 'dashboard/igrejas_dashboard.html',context)

 
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
    return render(request,'dashboard/igrejas_form.html',{'form':form})    

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
    return render(request,'dashboard/igrejas_form.html',{'form':form})  

def dashboard_igrejas_delete(request, igreja_id):
    igreja = Igreja.objects.get(id=igreja_id)
    try:
        igreja.delete()
    except:
        pass
    return redirect('dashboard_igrejas')    