from django import forms
from django.forms import widgets
from django.forms.widgets import TextInput,EmailInput



class Contactform(forms.Form):
    name = forms.CharField( required = True, widget= forms.TextInput(
        attrs={ 'class': 'form-control', 'placeholder': 'Nombre'}
    ))
    email = forms.EmailField(required =True, widget= forms.EmailInput(
        attrs = {'class': 'form-control', 'placeholder': 'Correo Electronico'}
    ))
    content = forms.CharField(required= True , widget = forms.Textarea(
        attrs = {'class': 'form-control', 'placeholder': 'Deje su mensaje'}
    ))
    
    
    
    
