from django.contrib import admin
from .models import Profile, NewProfile, Key


class ProfileAdmin(admin.ModelAdmin):
    model = Profile


class NewProfileAdmin(admin.ModelAdmin):
    model = NewProfile


class KeyAdmin(admin.ModelAdmin):
    model = Key


admin.site.register(Profile, ProfileAdmin)
admin.site.register(NewProfile, NewProfileAdmin)
admin.site.register(Key, KeyAdmin)
