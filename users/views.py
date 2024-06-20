from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .forms import *
import datetime
from django.contrib.auth.hashers import make_password
from .models import User
from django.contrib.auth.models import  Group, Permission
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

def get_grouped_permissions():
    # Get all permissions
    permissions = Permission.objects.all()
    # Group permissions by their content type (model)
    grouped_permissions = {}
    for perm in permissions:
        model = perm.content_type
        if model not in grouped_permissions:
            grouped_permissions[model] = []
        grouped_permissions[model].append(perm)
    
    # Convert content types to string keys
    permissions_by_model = {str(model): perms for model, perms in grouped_permissions.items()}
    
    return permissions_by_model
def register_customer(request):
    if request.method == 'POST':
        form = RegisterCustomer(request.POST)
        if form.is_valid():
            new=form.save(commit=False)
            new.is_customer=True
            new.save()
            messages.success(request,'Account created successfully')
            return redirect('/')
        else:
            messages.error(request,form.errors)
            return render(request,'register.html',{'form':form})
    else:
        form = RegisterCustomer()
    return render(request,'register.html',{'form':form})
# Create your views here.
def login_customer(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username, password=password)
        if user is not None and user.is_active:
            login(request,user)
            messages.success(request,'logged in')
            return redirect('/')
        else:
            messages.error(request, 'Invalid username or password.')
            return render(request,'login.html')
    else:
        return render(request,'login.html')
def logout_customer(request):
    logout(request)
    messages.success(request,'logged out ..')
    return redirect('login')
    
def show_users(request):
    if request.POST:
        form = UserForm(request.POST)
        if form.is_valid():
            new = form.save(commit=False)
            new.created_by = request.user
            new.is_active=True
            form.save()
            return redirect('/users')
        else:
            print(form.errors)
    context={
        "users": User.objects.all(),
        "fields": UserForm()
    }
    return render(request,'show_users.html',context)
def add_user(request):
    if request.POST:
        form = UserForm(request.POST)
        if form.is_valid():
            password = request.POST.get('password')
            password1 = request.POST.get('password1')
            if password==password1:
                new=form.save(commit=False)
                new.password = make_password(password)  # Encrypt the password
                new.is_active=True
                new.date_joined=datetime.datetime.now()
                form.save()
                messages.success(request,'New User ..')
                return redirect('/users')
            else:
                messages.error(request,"Password Dosen't Match ...")
                return render(request,'add_user.html',{'form':form})
        else:
            messages.error(request,'Error...')
            return render(request,'add_user.html',{'form':form})
    else:
        form = UserForm()
        return render(request,'add_user.html',{'form':form})

def delete_user(request,id):
    delete_Bank=get_object_or_404(User,id=id)
    if request.method == 'POST':
        delete_Bank.delete()
        messages.success(request, 'User Deleted ..')
        return redirect('/users')
    return render(request,'delete_user.html')

def add_edit_user_permissions(request, id):
    user = User.objects.get(id=id)
    if request.method == 'POST':
        form = UserFormPerm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            selected_permissions = request.POST.getlist('permissions')
            permissions = Permission.objects.filter(id__in=selected_permissions)
            user.user_permissions.set(permissions)
            return redirect('/users')
    else:
        form = UserFormPerm(instance=user)

    permissions_by_model = get_grouped_permissions()
    user_permissions_ids = user.user_permissions.values_list('id', flat=True)

    context = {
        'user': user,
        'form': form,
        'permissions_by_model': permissions_by_model,
        'user_permissions_ids': user_permissions_ids,
    }
    return render(request, 'add_edit_user_permissions.html', context)

def group_list(request):
    groups = Group.objects.all()
    return render(request, 'group_list.html', {'groups': groups})

def add_group(request):
    if request.method == 'POST':
        group_name = request.POST.get('group_name')
        new_group, created = Group.objects.get_or_create(name=group_name)
        selected_permissions = request.POST.getlist('permissions')
        permissions = Permission.objects.filter(id__in=selected_permissions)
        new_group.permissions.set(permissions)
        new_group.save()
        return redirect('/group_list')
    else:
        form = GroupForm()
        permissions_by_model = {}
        for permission in Permission.objects.all().select_related('content_type'):
            model = permission.content_type.model
            if model not in permissions_by_model:
                permissions_by_model[model] = []
            permissions_by_model[model].append(permission)

        # Pass the grouped permissions to the template
        context = {'permissions_by_model': permissions_by_model}
        return render(request, 'group_form.html', context)

def edit_group(request, id):
    # Get the group by ID
    group = Group.objects.get(id=id)
    
    # Get all permissions and group them by content type (model)
    permissions_by_model = get_grouped_permissions()
    
    # Get the IDs of the permissions that the group currently has
    group_permissions_ids = group.permissions.values_list('id', flat=True)
    
    # Pass the grouped permissions and the group's current data to the template
    context = {
        'permissions_by_model': permissions_by_model,
        'group_name': group.name,
        'group_permissions_ids': group_permissions_ids,
    }
    
    return render(request, 'edit_group.html', context)
