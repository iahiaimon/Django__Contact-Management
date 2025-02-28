from django import forms
from . import models

# from .models import ContactModel
# from home.models import ContactModel

class ContactForm(forms.ModelForm):
    class Meta:
        model = models.ContactModel
        fields = ['name' , 'phone' , 'email' , 'title' , 'image']
