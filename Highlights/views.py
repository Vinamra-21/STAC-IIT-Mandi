from django.shortcuts import render

# Create your views here.
def Highlights(request):
    return render(request, 'highlights.html')