from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.list import ListView

from .forms import(
    NameOfUser, 
    ChangeNicknameForm, 
    ChangeBioForm, 
    AddKeyForm,
    AddThisWeekForm,
    EditThisWeekForm,
    AddTodayForm,
    EditTodayForm
)
from .models import Profile, Key, ThisWeek, Today
	

class ProfilePageView(View):
	def get(self,request):
		return render(
            request, 
            'profile.html', 
            {'profile': Profile.objects.first()}
        )


class KeyPageView(ListView):
    model = Key
    template_name = "key.html"
	

class ThisWeekPageView(ListView):
    model = ThisWeek
    template_name = "thisweek.html"
	

class TodayPageView(ListView):
    model = Today
    template_name = "today.html"


def HomePageView(request):
	if request.method == 'POST':
		form = NameOfUser(request.POST)
		if form.is_valid():
			name = form.cleaned_data["name"]
			return render(
                request, 
                'index.html', 
                {'text': 'Hello {}! Today is going to be a great day!'.format(name)}
            )
	else:
		form = NameOfUser()
	return render(
        request, 
        'index.html', 
        {'form': form, 'text': 'Hello! What is your name?'}
    )


def ChangeNicknameView(request):
    profile = Profile.objects.first()
    if profile is None:
        profile = Profile.objects.create()
    if request.method =="POST":
        form = ChangeNicknameForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('/profile')
    else:
        form = ChangeNicknameForm()
    template = 'nickname_change.html'
    context = {'form': form}
    return render(request, template, context)


def ChangeBioView(request):
    profile = Profile.objects.first()
    if profile is None:
        profile = Profile.objects.create()
    if request.method =="POST":
        form = ChangeBioForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('/profile')
    else:
        form = ChangeBioForm()
    template = 'bio_change.html'
    context = {'form': form}
    return render(request, template, context)


def AddKeyView(request):
    if request.method == "POST":
        form = AddKeyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('key')
    else:
        form = AddKeyForm()
    template = 'add_key.html'
    context = {'form': form}
    return render(request, template, context)


def AddThisWeekView(request):
    if request.method == "POST":
        form = AddThisWeekForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('this_week')
    else:
        form=AddThisWeekForm()
    template = 'add_task_this_week.html'
    context = {'form': form}
    return render(request, template, context)


def EditThisWeekView(request, pk):
    task = get_object_or_404(ThisWeek, pk=pk)
    if request.method == "POST":
        form = EditThisWeekForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('this_week')
    else:
        form = EditThisWeekForm(instance=task)
    template = 'edit_task_this_week.html'
    context = {'task': task, 'form': form}
    return render(request, template, context)


def DeleteThisWeekView(request, pk):
    task = ThisWeek.objects.get(id=pk)
    task.delete()
    return redirect('this_week')


def DoneThisWeekView(request, pk):
    ThisWeek.objects.filter(id=pk).update(task_type='TASK DONE')
    return redirect('this_week')


def AddTodayView(request):
    if request.method == "POST":
        form = AddTodayForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('today')
    else:
        form=AddTodayForm()
    template = 'add_task_today.html'
    context = {'form': form}
    return render(request, template, context)


def EditTodayView(request, pk):
    task = get_object_or_404(Today, pk=pk)
    if request.method == "POST":
        form = EditTodayForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('today')
    else:
        form = EditTodayForm(instance=task)
    template = 'edit_task_today.html'
    context = {'task': task, 'form': form}
    return render(request, template, context)


def DeleteTodayView(request, pk):
    task = Today.objects.get(id=pk)
    task.delete()
    return redirect('today')


def DoneTodayView(request, pk):
    Today.objects.filter(id=pk).update(task_type='TASK DONE')
    return redirect('today')