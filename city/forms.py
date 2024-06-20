from django import forms
from employee.models import City
class CreateCityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = '__all__'

class UpdateCityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = '__all__'
