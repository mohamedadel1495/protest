from django import forms
from employee.models import Team
class CreateTeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = '__all__'

class UpdateTeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = '__all__'
