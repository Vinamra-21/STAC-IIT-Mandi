from django.db import models

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    full_description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='event_images/')
    date = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    register_link = models.URLField()

    def __str__(self):
        return self.title
