from django import forms
from employee.models import JobTitle
class CreateJobTitleForm(forms.ModelForm):
    class Meta:
        model = JobTitle
        fields = '__all__'

class UpdateJobTitleForm(forms.ModelForm):
    class Meta:
        model = JobTitle
        fields = '__all__'
