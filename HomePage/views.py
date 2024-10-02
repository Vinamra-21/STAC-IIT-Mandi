from django.shortcuts import render
from .models import Homepage, ClubActivity, Achievements, Links
# Create your views here.
def homepage(request):
    content={
        'homepage'=Homepage.objects.all()
        'achievements'=Achievements.objects.all()
        'link': Links.objects.all(),
    }
    return render(request, 'home.html' ,{'content':content})

def home(request):
    context_ = {
        "club_activity": club_activity.objects.all(),
        "competitions": homepage.objects.filter(id__in=(1, 2, 3, 4, 8)),
        "events_intro": homepage.objects.filter(id__in=(6, 5, 7)),
        "future_projects": homepage.objects.filter(id__in=(11, 10, 9, 12, 13, 14)),
        "introduction": homepage.objects.get(id__in=(15,)),
        "home": "active",
        "achievements": achievements.objects.all(),
        # "astrax": Links.objects.ffilter(linkname="astrax"),
        # "pleiades": Links.objects.filter(linkname="pleiades"),
        # "utkarsh": Links.objects.filter(linkname="utkarsh"),
        # "zenith": Links.objects.filter(linkname="zenith"),
        
    }
    return render(request, "stac_iitmandi/home.html", context_)
