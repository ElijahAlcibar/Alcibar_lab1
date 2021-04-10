from django.contrib import admin
from .models import Profile, NewProfile


class ProfileAdmin(admin.ModelAdmin):
    model = Profile

class NewProfileAdmin(admin.ModelAdmin):
    model = NewProfile

admin.site.register(Profile, ProfileAdmin)
admin.site.register(NewProfile, NewProfileAdmin)
