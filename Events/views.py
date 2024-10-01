from django.shortcuts import render
from .models import Event

# Create your views here.
def astrax(request):
    # events = Event.objects.all()
    return render(request, 'astrax.html')
# {'events': events}

def pleiades(request):
    return render(request, 'pleiades.html')

def utkarsh(request):
    return render(request, 'utkarsh.html')

def zenith(request):
    return render(request, 'zenith.html')