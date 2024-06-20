from typing import Any, Mapping
from django.contrib.auth.forms import UserCreationForm
from django import forms
from collections import defaultdict
from django.contrib.auth.models import Permission,Group
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from django.db.models import Q

from .models import *
class RegisterCustomer(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password','email','first_name']
        
class UserFormPerm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['groups', 'user_permissions', 'is_active']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Get all available permissions
        all_permissions = Permission.objects.all()
        # Get the user's current permissions
        user_permissions = self.instance.user_permissions.all()

        # Create a dictionary to track permission status (active or not)
        permission_status = {perm.id: perm in user_permissions for perm in all_permissions}

        # Add a BooleanField for each permission
        for perm in all_permissions:
            self.fields[f'permission_{perm.id}'] = forms.BooleanField(
                label=perm.name,
                required=False,
                initial=permission_status[perm.id],)

    def save(self, commit=True):
        user = super().save(commit=False)
        all_permissions = Permission.objects.all()
        for perm in all_permissions:
            field_name = f'permission_{perm.id}'
            if self.cleaned_data[field_name]:
                user.user_permissions.add(perm.id)
            else:
                user.user_permissions.remove(perm.id)
        if commit:
            user.save()
        return user



class UserPermissionForm(forms.ModelForm):
    add_permissions = forms.ModelMultipleChoiceField(
        queryset=Permission.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple
    )
    remove_permissions = forms.ModelMultipleChoiceField(
        queryset=Permission.objects.none(),
        required=False,
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = User
        fields = ['add_permissions', 'remove_permissions']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(UserPermissionForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['add_permissions'].queryset = Permission.objects.exclude(user=user)
            self.fields['remove_permissions'].queryset = user.user_permissions.all()
            # Set initial permissions
            self.fields['remove_permissions'].initial = user.user_permissions.all()
            
class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(GroupForm, self).__init__(*args, **kwargs)
        # Get all permissions with related content types
        permissions = Permission.objects.select_related('content_type').all()
        # Create a Q object to hold our queries
        permission_queries = Q()
        # Group permissions by app label and add to Q object
        for perm in permissions:
            app_label = perm.content_type.app_label
            permission_queries |= Q(content_type__app_label=app_label)
        
        # Use the Q object to filter permissions for each app label
        for app_label in set(permissions.values_list('content_type__app_label', flat=True)):
            self.fields[f'permissions_{app_label}'] = forms.ModelMultipleChoiceField(
                queryset=Permission.objects.filter(content_type__app_label=app_label),
                widget=forms.CheckboxSelectMultiple,
                required=False,
                label=app_label.replace('_', ' ').capitalize()
            )