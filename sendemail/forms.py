# sendemail/forms.py
from django import forms

class ContactForm(forms.Form):
    email = forms.EmailField(required=True)
    topic = forms.CharField(required=True)
    first_name = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)