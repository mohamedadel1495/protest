
from django.shortcuts import render,redirect,get_object_or_404
from .forms import *
from django.contrib import messages
# Create your views here.
def add_city(request):
    if request.POST:
        form = CreateCityForm(request.POST)
        if form.is_valid():
            new=form.save(commit=False)
            new.created_by=request.user
            new.status='active'
            form.save()
            messages.success(request,'New city ..')
            return redirect('/city')
        else:
            messages.error(request,'Error...')
            return render(request,'add_city.html',{'form':form})
    else:
        form = CreateCityForm()
        return render(request,'add_city.html',{'form':form})
def update_city(request,id):
    city=City.objects.get(id=id)
    if request.POST:
        form = UpdateCityForm(request.POST,instance=city)
        if form.is_valid():
            form.save()
            messages.success(request,'city Updated ...')
            return redirect('/city')
        else:
            messages.error(request,'Error..')
            return redirect('/city')
    else:
        form = UpdateCityForm(instance=city)
        return render(request,'update_city.html',{'form':form})
def show_city(request):
    if request.POST:
        form = CreateCityForm(request.POST)
        if form.is_valid():
            new = form.save(commit=False)
            new.created_by = request.user
            new.status = 'active'
            form.save()
            return redirect('/city')
        else:
            print(form.errors)
    context={
        "citys": City.objects.all(),

        "fields": CreateCityForm()
    }

    return render(request,'show_city.html',context)
def delete_city(request,id):
    delete_city=get_object_or_404(City,id=id)
    if request.method == 'POST':
        delete_city.delete()
        messages.success(request, 'city Deleted ..')
        return redirect('/city')
    return render(request,'delete_city.html')