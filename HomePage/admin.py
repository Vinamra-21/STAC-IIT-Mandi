from django.contrib import admin
from .models import ClubActivity, Projects, Achievements
# Register your models here.

admin.site.register(ClubActivity)
admin.site.register(Projects)
admin.site.register(Achievements)