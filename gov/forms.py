from django import forms
from employee.models import Gov
class CreateGovForm(forms.ModelForm):
    class Meta:
        model = Gov
        fields = '__all__'

class UpdateGovForm(forms.ModelForm):
    class Meta:
        model = Gov
        fields = '__all__'
