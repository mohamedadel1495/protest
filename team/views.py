
from django.shortcuts import render,redirect,get_object_or_404
from .forms import *
from django.contrib import messages
# Create your views here.
def add_team(request):
    if request.POST:
        form = CreateTeamForm(request.POST)
        if form.is_valid():
            new=form.save(commit=False)
            new.created_by=request.user
            new.status='active'
            form.save()
            messages.success(request,'New team ..')
            return redirect('/team')
        else:
            messages.error(request,'Error...')
            return render(request,'add_team.html',{'form':form})
    else:
        form = CreateTeamForm()
        return render(request,'add_team.html',{'form':form})
def update_team(request,id):
    team=Team.objects.get(id=id)
    if request.POST:
        form = UpdateTeamForm(request.POST,instance=team)
        if form.is_valid():
            form.save()
            messages.success(request,'team Updated ...')
            return redirect('/team')
        else:
            messages.error(request,'Error..')
            return redirect('/team')
    else:
        form = UpdateTeamForm(instance=team)
        return render(request,'update_team.html',{'form':form})
def show_team(request):
    if request.POST:
        form = CreateTeamForm(request.POST)
        if form.is_valid():
            new = form.save(commit=False)
            new.created_by = request.user
            new.status = 'active'
            form.save()
            return redirect('/team')
        else:
            print(form.errors)
    context={
        "teams": Team.objects.all(),
        "fields": CreateTeamForm()
    }
    return render(request,'show_team.html',context)
def delete_team(request,id):
    delete_team=get_object_or_404(Team,id=id)
    if request.method == 'POST':
        delete_team.delete()
        messages.success(request, 'Team Deleted ..')
        return redirect('/team')
    return render(request,'delete_team.html')