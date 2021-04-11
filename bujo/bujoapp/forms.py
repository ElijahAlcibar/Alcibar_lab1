from django import forms
from .models import Profile, Key, ThisWeek, Today

class NameOfUser(forms.Form):
	name = forms.CharField(label="", max_length=100)


class ChangePictureForm(forms.ModelForm):
	class Meta:
		model=Profile
		fields = ['picture']


class ChangeNicknameForm(forms.ModelForm):
	class Meta:
		model=Profile
		fields = ['nickname']


class ChangeBioForm(forms.ModelForm):
	class Meta:
		model=Profile
		fields = ['bio']


class AddKeyForm(forms.ModelForm):
	class Meta:
		model=Key
		fields = ['key', 'description']


class AddThisWeekForm(forms.ModelForm):
	class Meta:
		model = ThisWeek
		fields = ['task_type', 'task_description']


class EditThisWeekForm(forms.ModelForm):
	class Meta:
		model = ThisWeek
		fields = ['task_type', 'task_description']


class AddTodayForm(forms.ModelForm):
	class Meta:
		model = Today
		fields = ['task_type', 'task_description']


class EditTodayForm(forms.ModelForm):
	class Meta:
		model = Today
		fields = ['task_type', 'task_description']