from django.shortcuts import render,redirect,get_object_or_404
from .forms import *
from .models import *
from django.contrib import messages
import json
from django.http import JsonResponse
# Create your views here.
def add_employee(request):
    form = CreateEmployeeForm()
    selected_department_id = request.POST.get('department')
    if request.POST:
        form = CreateEmployeeForm(request.POST)
        form.fields['section'].queryset = Section.objects.filter(department_id=selected_department_id)
        if form.is_valid():
            new=form.save(commit=False)
            new.created_by=request.user
            new.status='active'
            form.save()
            messages.success(request,'New Employee ..')
            return redirect('/employee')
        else:
            messages.error(request,'Error...')
            return render(request,'add_employee.html',{'form':form})
    else:
        form = CreateEmployeeForm()
        return render(request,'add_employee.html',{'form':form})

def update_employee(request,id):
    employee=Employee.objects.get(id=id)
    if request.POST:
        form = UpdateEmployeeForm(request.POST,instance=employee)
        if form.is_valid():
            form.save()
            # message.success(request,'New Employee ..')
            return redirect('/employee')
        else:
            # message.error(request,'Error..')
            return redirect('update_employee')
    else:
        form = UpdateEmployeeForm(instance=employee)
        return render(request,'update_employee.html',{'form':form})
def show_employee(request):
    if request.POST:
        form = CreateEmployeeForm(request.POST)
        if form.is_valid():
            new = form.save(commit=False)
            new.created_by = request.user
            new.status = 'active'
            form.save()
            return redirect('/employee')
        else:
            print(form.errors)
    context={
        "employees": Employee.objects.all(),
        "fields": CreateEmployeeForm()
    }
    return render(request,'show_employee.html',context)
def delete_employee(request,id):
    delete_employee=get_object_or_404(Employee,id=id)
    if request.method == 'POST':
        delete_employee.delete()
        return redirect('/employee')
    return render(request,'delete_employee.html')
def load_sections(request):
    department_id = request.GET.get('department_id')
    sections = Section.objects.filter(department_id=department_id).order_by('name')
    return JsonResponse(list(sections.values('id', 'name')), safe=False)