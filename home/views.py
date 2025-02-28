from django.shortcuts import render , redirect
from django.http import HttpResponse
from . import models , forms


# Create your views here.
def home(request):
    return render(request , 'home.html')


def contact(request):
    form = forms.ContactForm()

    if request.method == 'POST':
        form = forms.ContactForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            return render(request , 'home.html')
            # return redirect('home')
    else:
        return render(request , 'form.html')
        # return redirect('form')

    return render(request, 'home.html')
