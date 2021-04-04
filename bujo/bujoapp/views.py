from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from .forms import NameOfUser

def HomePageView(request):
	if request.method == 'POST':
		form = NameOfUser(request.POST)
		if form.is_valid():
			return HttpResponse(
				"Hello, {}! Today is going to be a great day".format(
					form.cleaned_data['name']
				)
			)
	else:
		form = NameOfUser()
	return render(request, 'index.html', {'form': form})
