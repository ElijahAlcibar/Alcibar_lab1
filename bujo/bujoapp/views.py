from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from .forms import NameOfUser
	
class ProfilePageView(View):
	def get(self,request):
		return HttpResponse('profile.html')

def HomePageView(request):
	if request.method == 'POST':
		form = NameOfUser(request.POST)
		if form.is_valid():
			name = form.cleaned_data["name"]
			return render(request, 'index.html', {'text': 'Hello {} Today is going to be a great day!'.format(name)})
	else:
		form = NameOfUser()
	return render(request, 'index.html', {'form': form, 'text': 'Hello! What is your name?'})
