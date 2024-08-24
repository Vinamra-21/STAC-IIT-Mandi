from django.shortcuts import render
from .models import MemberDetail

# Create your views here.

def team_view(request):
    members = MemberDetail.objects.all()
    return render(request, 'coreTeamLayout.html', {'team_member': members})

def moreInfo(request):
    return render(request, 'website/moreInfo.html')