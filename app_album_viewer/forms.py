from django import forms
from .models import *

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['cover', 'title', 'description', 'artist', 'price', 'format', 'release_date']

        widgets = {
            'cover': forms.FileInput(attrs={
                'class': 'formfield',
            }),
            'title': forms.TextInput(attrs={
                'class': 'formfield',
                'placeholder': 'Album Title',
            }),
            'description': forms.Textarea(attrs={
                'class': 'formfield',
                'placeholder': 'Album Description'
            }),
            'artist': forms.TextInput(attrs={
                'class': 'formfield',
                'placeholder': 'Artist',
            }),
            'price': forms.NumberInput(attrs={
                'class': 'formfield',
                'placeholder': 'Price',
            }),
            'format': forms.Select(attrs={
                'class': 'formfield',
            }),
            'release_date': forms.DateInput(attrs={
                'class': 'formfield',
                'placeholder': 'Release Date (YYYY-MM-DD)',
                'style': 'width: 15%',
            }),
        }
