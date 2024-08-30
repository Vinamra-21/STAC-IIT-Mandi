from django.db import models

# Create your models here.

class Picture(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='gallery_pics/')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title or 'Untitled'
