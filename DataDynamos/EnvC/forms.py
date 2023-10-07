from django import forms
from .models import userfeed
from django.core import validators

class userfeed(forms.Form):
  
        name=forms.CharField(label="Your name", max_length=100)
        email=forms.EmailField(label="Your email")
        Feedback=forms.CharField(label="Your feedback", max_length=1000)
    





