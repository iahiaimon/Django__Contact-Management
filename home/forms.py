from django import forms
from . import models

class ContactForm(forms.ModelForm):
    class Meta:
        model = models.ContactModel
        fields = ['name' , 'phone' , 'email' , 'title' , 'image']
