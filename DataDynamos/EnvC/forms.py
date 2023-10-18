
from django import forms
from .models import *
from django.forms import ModelForm


class user(forms.ModelForm):
    name=forms.TextInput()
    email=forms.EmailField()
    location=forms.TextInput()
    Feedback=forms.TextInput()
    class Meta:
        model = userfeed
      
        fields = ("name", "email", "location", "Feedback")
    

    def __init__(self, *args, **kwargs):
        super(user, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'





class indus(forms.ModelForm):
    name=forms.TextInput()
    email=forms.EmailField()
    location=forms.TextInput()                  
    AboutIndustry=forms.TextInput()
    class Meta:
        model = indusfeed
        fields = ("name", "email", "location", "domain", "AboutIndustry")
    

    def __init__(self, *args, **kwargs):
        super(indus, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

     

           