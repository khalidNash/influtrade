from django import forms
from django.forms import ModelForm, TextInput, NumberInput
from personsManager.models import Contact

class ContactForm(forms.ModelForm):  
    class Meta:  
        model = Contact  
        fields = "__all__"  
        widgets = {
            'person_name': TextInput(attrs={
                'placeholder': 'Name goes here',
            }),
            'age': NumberInput(attrs={
                'placeholder': 'Age goes here',
            }),
        }