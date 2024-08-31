from django.shortcuts import render
from .models import Blogs

# Create your views here.
def Blog(request):
    blogs = Blogs.objects.all()
    return render(request, 'blog.html', {'blogs': blogs})

