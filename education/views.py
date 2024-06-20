
from django.shortcuts import render,redirect,get_object_or_404
from .forms import *
from django.contrib import messages
# Create your views here.
def add_education(request):
    if request.POST:
        form = CreateEducationForm(request.POST)
        if form.is_valid():
            new=form.save(commit=False)
            new.created_by=request.user
            new.status='active'
            form.save()
            messages.success(request,'New education ..')
            return redirect('/education')
        else:
            messages.error(request,'Error...')
            return render(request,'add_education.html',{'form':form})
    else:
        form = CreateEducationForm()
        return render(request,'add_education.html',{'form':form})
def update_education(request,id):
    education=Education.objects.get(id=id)
    if request.POST:
        form = UpdateEducationForm(request.POST,instance=education)
        if form.is_valid():
            form.save()
            messages.success(request,'education Updated ...')
            return redirect('/education')
        else:
            messages.error(request,'Error..')
            return redirect('/education')
    else:
        form = UpdateEducationForm(instance=education)
        return render(request,'update_education.html',{'form':form})
def show_education(request):
    if request.POST:
        form = CreateEducationForm(request.POST)
        if form.is_valid():
            new = form.save(commit=False)
            new.created_by = request.user
            new.status = 'active'
            form.save()
            return redirect('/education')
        else:
            print(form.errors)
    context={
        "educations": Education.objects.all(),
        "fields": CreateEducationForm()
    }
    return render(request,'show_education.html',context)
def delete_education(request,id):
    delete_education=get_object_or_404(Education,id=id)
    if request.method == 'POST':
        delete_education.delete()
        messages.success(request, 'education Deleted ..')
        return redirect('/education')
    return render(request,'delete_education.html')