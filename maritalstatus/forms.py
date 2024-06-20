from django import forms
from employee.models import MaritalStatus
class CreateMaritalStatusForm(forms.ModelForm):
    class Meta:
        model = MaritalStatus
        fields = '__all__'

class UpdateMaritalStatusForm(forms.ModelForm):
    class Meta:
        model = MaritalStatus
        fields = '__all__'

    # def __init__(self, *args, **kwargs):
    #     super(UpdateBankForm, self).__init__(*args, **kwargs)
    #     for field_name, field in self.fields.items():
    #         field.widget.attrs.update({'class': 'form-group form-control '})