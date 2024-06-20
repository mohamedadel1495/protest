
from django.shortcuts import render,redirect,get_object_or_404
from .forms import *
from django.contrib import messages
# Create your views here.
def add_college(request):
    if request.POST:
        form = CreateCollegeForm(request.POST)
        if form.is_valid():
            new=form.save(commit=False)
            new.created_by=request.user
            new.status='active'
            form.save()
            messages.success(request,'New college ..')
            return redirect('/college')
        else:
            messages.error(request,'Error...')
            return render(request,'add_college.html',{'form':form})
    else:
        form = CreateCollegeForm()
        return render(request,'add_college.html',{'form':form})
def update_college(request,id):
    college=College.objects.get(id=id)
    if request.POST:
        form = UpdateCollegeForm(request.POST,instance=college)
        if form.is_valid():
            form.save()
            messages.success(request,'college Updated ...')
            return redirect('/college')
        else:
            messages.error(request,'Error..')
            return redirect('/college')
    else:
        form = UpdateCollegeForm(instance=college)
        return render(request,'update_college.html',{'form':form})
def show_college(request):
    if request.POST:
        form = CreateCollegeForm(request.POST)
        if form.is_valid():
            new = form.save(commit=False)
            new.created_by = request.user
            new.status = 'active'
            form.save()
            return redirect('/college')
        else:
            print(form.errors)
    context={
        "colleges": College.objects.all(),

        "fields": CreateCollegeForm()
    }

    return render(request,'show_college.html',context)
def delete_college(request,id):
    delete_college=get_object_or_404(College,id=id)
    if request.method == 'POST':
        delete_college.delete()
        messages.success(request, 'college Deleted ..')
        return redirect('/college')
    return render(request,'delete_college.html')