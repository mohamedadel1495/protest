from django import forms
from employee.models import Education
class CreateEducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = '__all__'

class UpdateEducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = '__all__'
