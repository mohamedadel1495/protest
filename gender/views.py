from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect,get_object_or_404
from .forms import *
from django.contrib import messages
# Create your views here.
def add_gender(request):
    if request.POST:
        form = CreateGenderForm(request.POST)
        if form.is_valid():
            new=form.save(commit=False)
            new.created_by=request.user
            new.status='active'
            form.save()
            messages.success(request,'New gender ..')
            return redirect('/gender')
        else:
            messages.error(request,'Error...')
            return render(request,'add_gender.html',{'form':form})
    else:
        form = CreateGenderForm()
        return render(request,'add_gender.html',{'form':form})
def update_gender(request,id):
    gender=Gender.objects.get(id=id)
    if request.POST:
        form = UpdateGenderForm(request.POST,instance=gender)
        if form.is_valid():
            form.save()
            messages.success(request,'gender Updated ...')
            return redirect('/gender')
        else:
            messages.error(request,'Error..')
            return redirect('/gender')
    else:
        form = UpdateGenderForm(instance=gender)
        return render(request,'update_gender.html',{'form':form})
def show_gender(request):
    if request.POST:
        form = CreateGenderForm(request.POST)
        if form.is_valid():
            new = form.save(commit=False)
            new.created_by = request.user
            new.status = 'active'
            form.save()
            return redirect('/gender')
        else:
            print(form.errors)
    context={
        "genders": Gender.objects.all(),
        "fields": CreateGenderForm()
    }
    return render(request,'show_gender.html',context)
def delete_gender(request,id):
    delete_gender=get_object_or_404(Gender,id=id)
    if request.method == 'POST':
        delete_gender.delete()
        messages.success(request, 'gender Deleted ..')
        return redirect('/gender')
    return render(request,'delete_gender.html')