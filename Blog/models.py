from django.db import models

# Create your models here.
class Blogs(models.Model):
    title = models.CharField(max_length=200)
    short_description = models.TextField()
    thumbnail = models.ImageField(upload_to='blog_thumbnails/')
    editor_name = models.CharField(max_length=100)
    edited_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
