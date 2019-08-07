from django import forms
from django.forms import ModelForm, TextInput, NumberInput
from personsManager.models import Contact

class ContactForm(forms.ModelForm):  
    class Meta:  
        model = Contact  
        exclude = ('added_by',)  
        widgets = {
            'person_name': TextInput(attrs={
                'placeholder': 'Name goes here',
            }),
            'age': NumberInput(attrs={
                'placeholder': 'Age goes here',
            }),
        }


    def save(self, user):
        obj = super().save(commit = False)
        obj.added_by = user
        obj.save()
        return obj