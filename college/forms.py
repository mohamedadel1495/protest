from django import forms
from employee.models import College
class CreateCollegeForm(forms.ModelForm):
    class Meta:
        model = College
        fields = '__all__'

class UpdateCollegeForm(forms.ModelForm):
    class Meta:
        model = College
        fields = '__all__'
