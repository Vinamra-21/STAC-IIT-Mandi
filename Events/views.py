from django.shortcuts import render
from .models import Section

# Create your views here.
def Events(request):
    sections = Section.objects.all()
    return render(request, 'events.html', {'sections': sections})
