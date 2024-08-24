from django.db import models

# Create your models here.
class MemberDetail(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.CharField(max_length=100)
    linkedin_url  = models.CharField(max_length=100)
    instagram_url = models.CharField(max_length=100)
    image_url = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.name