from django import forms
from employee.models import Section
class CreateSectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = '__all__'
    def __init__(self,*args,**kwargs):
        super(CreateSectionForm,self).__init__(*args,**kwargs)
        for field_name,field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})
class UpdateSectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = '__all__'