from django.shortcuts import render

# Create your views here.
def Achievements(request):
    return render(request, 'achievements.html')