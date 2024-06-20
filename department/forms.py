from django import forms
from employee.models import Department
class CreateDepartmentForm(forms.ModelForm):

    class Meta:
        model = Department
        fields = '__all__'

class UpdateDepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'