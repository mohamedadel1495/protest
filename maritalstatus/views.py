from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect,get_object_or_404
from .forms import *
from django.contrib import messages
# Create your views here.
def add_maritalstatus(request):
    if request.POST:
        form = CreateMaritalStatusForm(request.POST)
        if form.is_valid():
            new=form.save(commit=False)
            new.created_by=request.user
            new.status='active'
            form.save()
            messages.success(request,'New maritalstatus ..')
            return redirect('/maritalstatus')
        else:
            messages.error(request,'Error...')
            return render(request,'add_maritalstatus.html',{'form':form})
    else:
        form = CreateMaritalStatusForm()
        return render(request,'add_maritalstatus.html',{'form':form})
def update_maritalstatus(request,id):
    maritalstatus=MaritalStatus.objects.get(id=id)
    if request.POST:
        form = UpdateMaritalStatusForm(request.POST,instance=maritalstatus)
        if form.is_valid():
            form.save()
            messages.success(request,'maritalstatus Updated ...')
            return redirect('/maritalstatus')
        else:
            messages.error(request,'Error..')
            return redirect('/maritalstatus')
    else:
        form = UpdateMaritalStatusForm(instance=maritalstatus)
        return render(request,'update_maritalstatus.html',{'form':form})
def show_maritalstatus(request):
    if request.POST:
        form = CreateMaritalStatusForm(request.POST)
        if form.is_valid():
            new = form.save(commit=False)
            new.created_by = request.user
            new.status = 'active'
            form.save()
            return redirect('/maritalstatus')
        else:
            print(form.errors)
    context={
        "maritalstatuss": MaritalStatus.objects.all(),
        "fields": CreateMaritalStatusForm()
    }
    return render(request,'show_maritalstatus.html',context)
def delete_maritalstatus(request,id):
    delete_maritalstatus=get_object_or_404(MaritalStatus,id=id)
    if request.method == 'POST':
        delete_maritalstatus.delete()
        messages.success(request, 'maritalstatus Deleted ..')
        return redirect('/maritalstatus')
    return render(request,'delete_maritalstatus.html')