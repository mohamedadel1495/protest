# Create your views here.
from django.shortcuts import render,redirect,get_object_or_404
from .forms import *
from django.contrib import messages
# Create your views here.
def add_jobtitle(request):
    if request.POST:
        form = CreateJobTitleForm(request.POST)
        if form.is_valid():
            new=form.save(commit=False)
            new.created_by=request.user
            new.status='active'
            form.save()
            messages.success(request,'New jobtitle ..')
            return redirect('/jobtitle')
        else:
            messages.error(request,'Error...')
            return render(request,'add_jobtitle.html',{'form':form})
    else:
        form = CreateJobTitleForm()
        return render(request,'add_jobtitle.html',{'form':form})
def update_jobtitle(request,id):
    jobtitle=JobTitle.objects.get(id=id)
    if request.POST:
        form = UpdateJobTitleForm(request.POST,instance=jobtitle)
        if form.is_valid():
            form.save()
            messages.success(request,'jobtitle Updated ...')
            return redirect('/jobtitle')
        else:
            messages.error(request,'Error..')
            return redirect('/jobtitle')
    else:
        form = UpdateJobTitleForm(instance=jobtitle)
        return render(request,'update_jobtitle.html',{'form':form})
def show_jobtitle(request):
    if request.POST:
        form = CreateJobTitleForm(request.POST)
        if form.is_valid():
            new = form.save(commit=False)
            new.created_by = request.user
            new.status = 'active'
            form.save()
            return redirect('/jobtitle')
        else:
            print(form.errors)
    context={
        "jobtitles": JobTitle.objects.all(),
        "fields": CreateJobTitleForm()
    }
    return render(request,'show_jobtitle.html',context)
def delete_jobtitle(request,id):
    delete_jobtitle=get_object_or_404(JobTitle,id=id)
    if request.method == 'POST':
        delete_jobtitle.delete()
        messages.success(request, 'jobtitle Deleted ..')
        return redirect('/jobtitle')
    return render(request,'delete_jobtitle.html')