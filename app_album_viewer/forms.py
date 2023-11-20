from django import forms
from .models import Album

# creating a form
class AlbumForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
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