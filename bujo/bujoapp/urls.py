from django.urls import path

from .views import HomePageView, ProfilePageView

urlpatterns = [
	path('home', HomePageView, name='home'),
	path('profile', ProfilePageView.as_view(), name='profile'),
]
