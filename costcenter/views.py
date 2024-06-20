
from django.shortcuts import render,redirect,get_object_or_404
from .forms import *
from django.contrib import messages
# Create your views here.
def add_costcenter(request):
    if request.POST:
        form = CreateCostCenterForm(request.POST)
        if form.is_valid():
            new=form.save(commit=False)
            new.created_by=request.user
            new.status='active'
            form.save()
            messages.success(request,'New costcenter ..')
            return redirect('/costcenter')
        else:
            messages.error(request,'Error...')
            return render(request,'add_costcenter.html',{'form':form})
    else:
        form = CreateCostCenterForm()
        return render(request,'add_costcenter.html',{'form':form})
def update_costcenter(request,id):
    costcenter=CostCenter.objects.get(id=id)
    if request.POST:
        form = UpdateCostCenterForm(request.POST,instance=costcenter)
        if form.is_valid():
            form.save()
            messages.success(request,'costcenter Updated ...')
            return redirect('/costcenter')
        else:
            messages.error(request,'Error..')
            return redirect('/costcenter')
    else:
        form = UpdateCostCenterForm(instance=costcenter)
        return render(request,'update_costcenter.html',{'form':form})
def show_costcenter(request):
    if request.POST:
        form = CreateCostCenterForm(request.POST)
        if form.is_valid():
            new = form.save(commit=False)
            new.created_by = request.user
            new.status = 'active'
            form.save()
            return redirect('/costcenter')
        else:
            print(form.errors)
    context={
        "costcenters": CostCenter.objects.all(),
        "fields": CreateCostCenterForm()
    }
    return render(request,'show_costcenter.html',context)
def delete_costcenter(request,id):
    delete_costcenter=get_object_or_404(CostCenter,id=id)
    if request.method == 'POST':
        delete_costcenter.delete()
        messages.success(request, 'costcenter Deleted ..')
        return redirect('/costcenter')
    return render(request,'delete_costcenter.html')