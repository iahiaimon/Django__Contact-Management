from django.shortcuts import render , redirect
from django.http import HttpResponse
from . import models , forms


# Create your views here.
def home(requaest):
    return render(requaest , 'home.html')


def contact(requaest):
    form = forms.ContactForm()

    if requaest.methon == 'POST':
        form = form.ContactForm(requaest.POST , requaest.FILES)
        if form.is_valid():
            form.save()
            return render(requaest , 'home.html')
    else:
        return render(requaest , 'form.html')

    return render(requaest, 'home.html')
