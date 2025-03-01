from django.db import models

# Create your models here.

class ContactModel(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20 , unique=True)
    email = models.EmailField(max_length=100 , unique=True)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='home/Image' , blank=True , null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    


    def __str__(self):
        return self.name



