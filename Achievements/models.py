from django.db import models
from django.utils import timezone
# Create your models here.

class Achievements(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='achievement_images/')
    tag = models.CharField(max_length=50, blank=True)
    def __str__(self):
        return self.title
