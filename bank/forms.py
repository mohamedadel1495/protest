from django import forms
from employee.models import Bank
class CreateBankForm(forms.ModelForm):
    class Meta:
        model = Bank
        fields = '__all__'
    # def __init__(self,*args,**kwargs):
    #     super(CreateBankForm,self).__init__(*args,**kwargs)
    #     for field_name,field in self.fields.items():
    #         field.widget.attrs.update({'class':'form-group form-control'})

        # def __init__(self, *args, **kwargs):
        #     super(CreateBankForm, self).__init__(*args, **kwargs)
        #     for name, field in self.fields.items():
        #         widget = field.widget
        #     if isinstance(field, forms.DateField):
        #         self.fields[name].widget = forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
        #     if isinstance(widget, (forms.CheckboxSelectMultiple, forms.CheckboxInput)):
        #         widget.attrs['class'] = 'form-check'
        #     else:
        #         widget.attrs['class'] = 'form-control'


class UpdateBankForm(forms.ModelForm):
    class Meta:
        model = Bank
        fields = '__all__'

    # def __init__(self, *args, **kwargs):
    #     super(UpdateBankForm, self).__init__(*args, **kwargs)
    #     for field_name, field in self.fields.items():
    #         field.widget.attrs.update({'class': 'form-group form-control '})

