from django import forms

# from . import models , views
from .models import ContactModel

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        feilds = ['name' , 'phone' , 'email' , 'title' , 'image']
