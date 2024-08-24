from django.urls import path ,include
from . import views

urlpatterns = [
    path('', views.CoreTeam, name='CoreTeam'),
    path('moreInfo', views.moreInfo, name='moreinfo'),
]