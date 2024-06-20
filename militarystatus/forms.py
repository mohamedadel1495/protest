from django import forms
from employee.models import MilitaryStatus
class CreateMilitaryStatusForm(forms.ModelForm):
    class Meta:
        model = MilitaryStatus
        fields = '__all__'

class UpdateMilitaryStatusForm(forms.ModelForm):
    class Meta:
        model = MilitaryStatus
        fields = '__all__'
