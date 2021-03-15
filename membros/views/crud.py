from django.shortcuts import render
from membros.forms import JovemCreateForm
from membros.models import Jovens
from django.core.paginator import Paginator
from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.core.paginator import Paginator


def dashboard_jovens(request):
    jovens = Jovens.objects.all()
    paginator = Paginator(jovens,9)

    page = request.GET.get('p')
    jovens = paginator.get_page(page)     
    context = {
        'jovens':jovens
    }
    return render(request, 'dashboard/membros/jovens_dashboard.html',context)


def dashboard_jovens_create(request):  
    if request.method == "POST":  
        form = JovemCreateForm(request.POST, request.FILES)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('dashboard_jovens')  
            except:  
                pass  
    else:  
        form = JovemCreateForm()  
    return render(request,'dashboard/membros/jovens_form.html',{'form':form})    


def dashboard_jovens_update(request, jovem_id):  
    jovem = Jovens.objects.get(id=jovem_id)
    form = JovemCreateForm()
    if request.method == "POST":  
        form = JovemCreateForm(request.POST,request.FILES, instance=jovem)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('dashboard_jovens')  
            except Exception as e: 
                pass    
    return render(request,'dashboard/membros/jovens_form.html',{'form':form})  


def dashboard_jovens_delete(request, jovem_id):
    jovens = Jovens.objects.get(id=jovem_id)
    try:
        jovens.delete()
    except:
        pass
    return redirect('dashboard_jovens')
