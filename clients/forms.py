from django import forms
from django.forms import ModelForm
from .models import Vendor

class VendorForm(ModelForm):
    class Meta:
        model = Vendor
        
        fields = ('name', 'domain', 'emailformat', 'country')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'domain': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Domain'}),
            'emailformat': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Format'}),
            'country': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Country'}),
            
        }