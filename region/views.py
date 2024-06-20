# Create your views here.
from django.shortcuts import render,redirect,get_object_or_404
from .forms import *
from django.contrib import messages
# Create your views here.
def add_region(request):
    if request.POST:
        form = CreateRegionForm(request.POST)
        if form.is_valid():
            new=form.save(commit=False)
            new.created_by=request.user
            new.status='active'
            form.save()
            messages.success(request,'New region ..')
            return redirect('/region')
        else:
            messages.error(request,'Error...')
            return render(request,'add_region.html',{'form':form})
    else:
        form = CreateRegionForm()
        return render(request,'add_region.html',{'form':form})
def update_region(request,id):
    region=Region.objects.get(id=id)
    if request.POST:
        form = UpdateRegionForm(request.POST,instance=region)
        if form.is_valid():
            form.save()
            messages.success(request,'region Updated ...')
            return redirect('/region')
        else:
            messages.error(request,'Error..')
            return redirect('/region')
    else:
        form = UpdateRegionForm(instance=region)
        return render(request,'update_region.html',{'form':form})
def show_region(request):
    if request.POST:
        form = CreateRegionForm(request.POST)
        if form.is_valid():
            new = form.save(commit=False)
            new.created_by = request.user
            new.status = 'active'
            form.save()
            return redirect('/region')
        else:
            print(form.errors)
    context={
        "regions": Region.objects.all(),
        "fields": CreateRegionForm()
    }
    return render(request,'show_region.html',context)
def delete_region(request,id):
    delete_region=get_object_or_404(Region,id=id)
    if request.method == 'POST':
        delete_region.delete()
        messages.success(request, 'region Deleted ..')
        return redirect('/region')
    return render(request,'delete_region.html')