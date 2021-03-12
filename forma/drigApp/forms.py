from django import forms
from .models import Emloeer


class EmploeerForm(forms.ModelForm):
    class Meta:
        model = Emloeer
        fields = ['name', 'contact', 'email']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'contact': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

