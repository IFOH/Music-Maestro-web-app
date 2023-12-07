from django import forms
from .models import *

class LoginForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput())

class EmailForm(forms.Form):
    recipient_email = forms.EmailField(required=True,label="To:")
    subject = forms.CharField(required=True,label="Subject:")
    message = forms.CharField(widget=forms.Textarea,required=True,label="Message:")
