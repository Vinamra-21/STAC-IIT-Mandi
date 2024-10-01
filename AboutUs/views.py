from django.shortcuts import render
from .models import Coordinator, GeneralContact

# Create your views here.
def AboutUs(request):
    # coordinators = Coordinator.objects.all()
    # general_contact = GeneralContact.objects.first() 
    return render(request, 'aboutus.html', )
# {'coordinators': coordinators, 'general_contact': general_contact}