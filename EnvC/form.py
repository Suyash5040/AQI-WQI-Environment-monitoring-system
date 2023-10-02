from django import forms

class feedbackForm(forms.Form):
    name=forms.CharField(label="Enter name", max_length=100)
    email=forms.EmailField(label="Enter email", max_length=100)
    feedback=forms.CharField(label="Your feedback", widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(feedbackForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'