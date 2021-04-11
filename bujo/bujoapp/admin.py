from django.contrib import admin
from .models import Profile, NewProfile, Key, ThisWeek


class ProfileAdmin(admin.ModelAdmin):
    model = Profile


class NewProfileAdmin(admin.ModelAdmin):
    model = NewProfile


class KeyAdmin(admin.ModelAdmin):
    model = Key


class ThisWeekAdmin(admin.ModelAdmin):
    model = ThisWeek


admin.site.register(Profile, ProfileAdmin)
admin.site.register(NewProfile, NewProfileAdmin)
admin.site.register(Key, KeyAdmin)
admin.site.register(ThisWeek, ThisWeekAdmin)

