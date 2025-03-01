from django.shortcuts import render , redirect
from django.http import HttpResponse
from . import models , forms


# Create your views here.
def home(request):
    users = models.ContactModel.objects.all()
    return render(request , 'home.html' , {'users' : users})


def contact(request):
    form = forms.ContactForm()

    if request.method == 'POST':
        form = forms.ContactForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            # return render(request , 'home.html')
            return redirect('home')
    else:
        return render(request , 'form.html' , {'form': form})
        # return redirect('form')

    return render(request, 'home.html')


def update(request , id):
    user = models.ContactModel.objects.get(id = id)
    form = forms.ContactForm(instance=user)

    if request.method == 'POST':
        form = forms.ContactForm(request.POST , request.FILES , instance=user)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        return render(request , 'form.html' , {'form': form , "edit" : True})
    

def delete(request , id):
    user = models.ContactModel.objects.get(id = id)
    user.delete()
    return redirect('home')
    
    # return render(request , 'home.html , ')