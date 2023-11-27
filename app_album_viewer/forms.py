from django import forms
from .models import *

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'formfield',
                'placeholder': 'Album Title',
            }),
            'description': forms.Textarea(attrs={
                'class': 'formfield',
                'placeholder': 'Album Description',
                'rows' : 25,
                'cols' : 60,
            }),
        }
