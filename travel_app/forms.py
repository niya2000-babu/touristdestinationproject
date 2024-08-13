# destinations/forms.py
from django import forms
from .models import Destination

class DestinationForm(forms.ModelForm):
    class Meta:
        model = Destination
        fields = ['place_name', 'weather', 'state', 'district', 'google_map_link', 'image', 'description']
        widgets = {
            'place_name': forms.TextInput(attrs={'class': 'form-control'}),
            'weather': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'district': forms.TextInput(attrs={'class': 'form-control'}),
            'google_map_link': forms.URLInput(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }
