from django.shortcuts import render

# Create your views here.
def AboutUs(request):
    return render(request, 'layout.html')