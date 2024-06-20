from django import forms
from .models import *
from django.core.exceptions import ValidationError

class CreateEmployeeForm(forms.ModelForm):
    section = forms.ModelChoiceField(queryset=Section.objects.none(), required=False)

    def __init__(self, *args, **kwargs):
        department_id = kwargs.pop('department_id', None)
        super(CreateEmployeeForm, self).__init__(*args, **kwargs)
        if department_id:
            self.fields['section'].queryset = Section.objects.filter(department_id=department_id)
        else:
            self.fields['section'].queryset = Section.objects.none()

    class Meta:
        model = Employee
        fields = '__all__'
class UpdateEmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'