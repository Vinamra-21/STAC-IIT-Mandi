from django.shortcuts import render
from .models import Achievements
# Create your views here.
def AchievementsList(request):
    achievements=Achievements.objects.all()
    return render(request, 'achievements.html',{'achievements':achievements})