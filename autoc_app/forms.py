from django import forms
from django.forms import fields, widgets
from . models import Client

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'name',
                'placeholder': 'Enter your Name'
            }),
            }