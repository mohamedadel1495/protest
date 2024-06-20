from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect,get_object_or_404
from .forms import *
from django.contrib import messages
# Create your views here.
def add_section(request):
    if request.POST:
        form = CreateSectionForm(request.POST)
        if form.is_valid():
            new=form.save(commit=False)
            new.created_by=request.user
            new.status='active'
            form.save()
            messages.success(request,'New section ..')
            return redirect('/section')
        else:
            messages.error(request,'Error...')
            return render(request,'add_section.html',{'form':form})
    else:
        form = CreateSectionForm()
        return render(request,'add_section.html',{'form':form})
def update_section(request,id):
    section=Section.objects.get(id=id)
    if request.POST:
        form = UpdateSectionForm(request.POST,instance=section)
        if form.is_valid():
            form.save()
            messages.success(request,'Section Updated ...')
            return redirect('/section')
        else:
            messages.error(request,'Error..')
            return redirect('/section')
    else:
        form = UpdateSectionForm(instance=section)
        return render(request,'update_section.html',{'form':form})
def show_section(request):
    if request.POST:
        form = CreateSectionForm(request.POST)
        if form.is_valid():
            new = form.save(commit=False)
            new.created_by = request.user
            new.status = 'active'
            form.save()
            return redirect('/section')
        else:
            print(form.errors)
    context={
        "sections": Section.objects.all(),
        "fields": CreateSectionForm()
    }
    return render(request,'show_section.html',context)
def delete_section(request,id):
    delete_section=get_object_or_404(Section,id=id)
    if request.method == 'POST':
        delete_section.delete()
        messages.success(request, 'Section Deleted ..')
        return redirect('/section')
    return render(request,'delete_section.html')