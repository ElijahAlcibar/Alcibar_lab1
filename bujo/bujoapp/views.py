from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from .forms import NameOfUser, NicknameProfileForm
from .models import ProfilePageModel
	
class ProfilePageView(View):
	def get(self,request):
		return render(request, 'profile.html')
	
class KeyPageView(View):
	def get(self,request):
		return render(request, 'key.html')
	
class ThisWeekPageView(View):
	def get(self,request):
		return render(request, 'thisweek.html')
	
class TodayPageView(View):
	def get(self,request):
		return render(request, 'today.html')

def HomePageView(request):
	if request.method == 'POST':
		form = NameOfUser(request.POST)
		if form.is_valid():
			name = form.cleaned_data["name"]
			return render(request, 'index.html', {'text': 'Hello {}! Today is going to be a great day!'.format(name)})
	else:
		form = NameOfUser()
	return render(request, 'index.html', {'form': form, 'text': 'Hello! What is your name?'})


def nickname_change(request):
	profile = ProfilePageModel.objects.first()
	if profile is None:
		profile = ProfilePageModel.objects.create()
	if request.method == "POST":
		form = NicknameProfileForm(request.POST, instance=profile)
		if form.is_valid():
			form.save()
			return redirect('profile')
	else:
		form = NicknameProfileForm()
	template = 'nickname_change.html'
	context = {'form': form}
	return render(request, template, context)