from django.db import models

# Create your models here.
class Section(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='section_images/')

    def __str__(self):
        return self.title