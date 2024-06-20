
# Create your views here.
from django.shortcuts import render,redirect,get_object_or_404,get_list_or_404
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.
@login_required
@permission_required('employee.add_bank', raise_exception=True)
def add_bank(request):
    if request.POST:
        form = CreateBankForm(request.POST)
        if form.is_valid():
            new=form.save(commit=False)
            new.created_by=request.user
            new.status='active'
            form.save()
            messages.success(request,'New Bank ..')
            return redirect('/bank')
        else:
            messages.error(request,'Error...')
            return render(request,'add_bank.html',{'form':form})
    else:
        form = CreateBankForm()
        return render(request,'add_bank.html',{'form':form})
@login_required
@permission_required('employee.change_bank', raise_exception=True)   
def update_bank(request,id):
    bank=Bank.objects.get(id=id)
    if request.POST:
        form = UpdateBankForm(request.POST,instance=bank)
        if form.is_valid():
            form.save()
            messages.success(request,'Bank Updated ...')
            return redirect('/bank')
        else:
            messages.error(request,'Error..')
            return redirect('/bank')
    else:
        form = UpdateBankForm(instance=bank)
        return render(request,'update_bank.html',{'form':form})
    

@login_required
@permission_required('employee.view_bank', raise_exception=True)
def show_bank(request):
    if request.POST:
        form = CreateBankForm(request.POST)
        if form.is_valid():
            new = form.save(commit=False)
            new.created_by = request.user
            new.status = 'active'
            form.save()
            return redirect('/bank')
        else:
            print(form.errors)
    context={
        "banks": Bank.objects.all(),
        "fields": CreateBankForm()
    }
    return render(request,'show_bank.html',context)


@login_required
@permission_required('employee.delete_bank', raise_exception=True)
def delete_bank(request,id):
    delete_Bank=get_object_or_404(Bank,id=id)
    if request.method == 'POST':
        delete_Bank.delete()
        messages.success(request, 'Bank Deleted ..')
        return redirect('/bank')
    return render(request,'delete_bank.html')
