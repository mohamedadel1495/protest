
from django.shortcuts import render,redirect,get_object_or_404
from .forms import *
from django.contrib import messages
# Create your views here.
def add_militarystatus(request):
    if request.POST:
        form = CreateMilitaryStatusForm(request.POST)
        if form.is_valid():
            new=form.save(commit=False)
            new.created_by=request.user
            new.status='active'
            form.save()
            messages.success(request,'New militarystatus ..')
            return redirect('/militarystatus')
        else:
            messages.error(request,'Error...')
            return render(request,'add_militarystatus.html',{'form':form})
    else:
        form = CreateMilitaryStatusForm()
        return render(request,'add_militarystatus.html',{'form':form})
def update_militarystatus(request,id):
    militarystatus=MilitaryStatus.objects.get(id=id)
    if request.POST:
        form = UpdateMilitaryStatusForm(request.POST,instance=militarystatus)
        if form.is_valid():
            form.save()
            messages.success(request,'militarystatus Updated ...')
            return redirect('/militarystatus')
        else:
            messages.error(request,'Error..')
            return redirect('/militarystatus')
    else:
        form = UpdateMilitaryStatusForm(instance=militarystatus)
        return render(request,'update_militarystatus.html',{'form':form})
def show_militarystatus(request):
    if request.POST:
        form = CreateMilitaryStatusForm(request.POST)
        if form.is_valid():
            new = form.save(commit=False)
            new.created_by = request.user
            new.status = 'active'
            form.save()
            return redirect('/militarystatus')
        else:
            print(form.errors)
    context={
        "militarystatuss": MilitaryStatus.objects.all(),
        "fields": CreateMilitaryStatusForm()
    }
    return render(request,'show_militarystatus.html',context)
def delete_militarystatus(request,id):
    delete_militarystatus=get_object_or_404(MilitaryStatus,id=id)
    if request.method == 'POST':
        delete_militarystatus.delete()
        messages.success(request, 'militarystatus Deleted ..')
        return redirect('/militarystatus')
    return render(request,'delete_militarystatus.html')