from django.shortcuts import render


# Create your views here.
def CoreTeam(request):
    team_member = {
        'name': 'John Doe',
        'image_url': 'https://picsum.photos/200/300',
        'message': 'https://picsum.photos/200/300',
        'instagram_url': 'https://www.instagram.com/username',
        'linkedin_url': 'https://www.linkedin.com/in/username',
    }
    return render(request, 'coreTeamLayout.html', {'team_member': team_member})


def moreInfo(request):
    return render(request, 'website/moreInfo.html')