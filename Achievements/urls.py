from django.urls import path
from . import views

urlpatterns = [
    path('', views.AchievementsList, name='achievements'),
]