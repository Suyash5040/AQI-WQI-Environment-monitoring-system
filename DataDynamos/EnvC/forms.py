
from django import forms
from .models import userfeed
from django.forms import ModelForm



   

class user(forms.ModelForm):
    name=forms.TextInput()
    email=forms.EmailField()
    Feedback=forms.TextInput()
    class Meta:
        model = userfeed
        fields = ("name", "email", "Feedback")
    

    def __init__(self, *args, **kwargs):
        super(user, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


        for field in self.fields.values(): 
            field.error_messages = {'required': 'The field {fieldname} is required'.format( fieldname=field.label)}

           