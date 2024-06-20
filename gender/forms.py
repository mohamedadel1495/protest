from django import forms
from employee.models import Gender
class CreateGenderForm(forms.ModelForm):
    class Meta:
        model = Gender
        fields = '__all__'
    def __init__(self,*args,**kwargs):
        super(CreateGenderForm,self).__init__(*args,**kwargs)
        for field_name,field in self.fields.items():
            field.widget.attrs.update({'class':'form-group form-control'})
class UpdateGenderForm(forms.ModelForm):
    class Meta:
        model = Gender
        fields = '__all__'

    # def __init__(self, *args, **kwargs):
    #     super(UpdateGenderForm, self).__init__(*args, **kwargs)
    #     for field_name, field in self.fields.items():
    #         field.widget.attrs.update({'class': 'form-group form-control '})