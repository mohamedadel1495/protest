from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect,get_object_or_404
from .forms import *
from .models import *
# Create your views here.
def add_dep(request):
    if request.POST:
        form = CreateDepartmentForm(request.POST)
        if form.is_valid():
            new=form.save(commit=False)
            new.created_by=request.user
            new.status='active'
            form.save()
            # message.success(request,'New dep ..')
            return redirect('/department')
        else:
            # message.error(request,'Error..')
            return render(request,'add_dep.html',{'form':form})
    else:
        form = CreateDepartmentForm()
        return render(request,'add_dep.html',{'form':form})
def update_dep(request,id):
    dep=Department.objects.get(id=id)
    print(dep)
    if request.POST:
        form = UpdateDepartmentForm(request.POST,instance=dep)
        if form.is_valid():
            form.save()
            # message.success(request,'New dep ..')
            return redirect('/department')
        else:
            # message.error(request,'Error..')
            return redirect('/department')
    else:
        form = UpdateDepartmentForm(instance=dep)
        return render(request,'update_dep.html',{'form':form})
def show_dep(request):
    if request.POST:
        form = CreateDepartmentForm(request.POST)
        if form.is_valid():
            new = form.save(commit=False)
            new.created_by = request.user
            new.status = 'active'
            form.save()
            return redirect('/department')
        else:
            print(form.errors)
    context={
        "deps": Department.objects.all(),
        "fields": CreateDepartmentForm()
    }
    return render(request,'show_dep.html',context)
def delete_dep(request,id):
    delete_dep=get_object_or_404(Department,id=id)
    if request.method == 'POST':
        delete_dep.delete()
        return redirect('/department')
    return render(request,'delete_dep.html')


def delete_selected(request):
    for id, name in request.POST.items():
        # delete action
        dep= Department.objects.filter(pk=id).first()
        if (dep):
            dep.delete()

    return HttpResponse(
        status=204,
        headers={
            'HX-Trigger': json.dumps({
                "bookListChanged": None,
                "showMessage": f"Selected Department is deleted"
            })
        })