from django import forms
from employee.models import Region
class CreateRegionForm(forms.ModelForm):
    class Meta:
        model = Region
        fields = '__all__'
    # def __init__(self,*args,**kwargs):
    #     super(CreateRegionForm,self).__init__(*args,**kwargs)
    #     for field_name,field in self.fields.items():
    #         field.widget.attrs.update({'class':'form-group form-control'})
class UpdateRegionForm(forms.ModelForm):
    class Meta:
        model = Region
        fields = '__all__'

    # def __init__(self, *args, **kwargs):
    #     super(UpdateBankForm, self).__init__(*args, **kwargs)
    #     for field_name, field in self.fields.items():
    #         field.widget.attrs.update({'class': 'form-group form-control '})