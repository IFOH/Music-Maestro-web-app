from django import forms
from .models import *

class LoginForm(forms.Form):
    username = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'style': 'width: 20%'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'style': 'width: 20%'}))

class EmailForm(forms.Form):
    recipient_email = forms.EmailField(required=True,label="To:", widget=forms.EmailInput(attrs={'style': 'width: 75%'}))
    subject = forms.CharField(required=True,label="Subject:", widget=forms.TextInput(attrs={'style': 'width: 75%'}))
    message = forms.CharField(required=True,label="Message:", widget=forms.Textarea(attrs={'style': 'width: 75%'}))
