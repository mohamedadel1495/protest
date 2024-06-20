from django import forms
from employee.models import CostCenter
class CreateCostCenterForm(forms.ModelForm):
    class Meta:
        model = CostCenter
        fields = '__all__'

class UpdateCostCenterForm(forms.ModelForm):
    class Meta:
        model = CostCenter
        fields = '__all__'
