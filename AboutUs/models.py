from django.db import models

# Create your models here.
class Coordinator(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    photo = models.ImageField(upload_to='coordinator_photos/')
    
    def __str__(self):
        return self.name

class GeneralContact(models.Model):
    address = models.TextField()
    name1 = models.CharField(max_length=100)
    name2 = models.CharField(max_length=100)
    phone_number1 = models.CharField(max_length=20)
    phone_number2 = models.CharField(max_length=20)
    email = models.EmailField()
    
    def __str__(self):
        return "General Contact Information"
