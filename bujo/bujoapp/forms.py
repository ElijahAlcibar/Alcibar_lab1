from django import forms
from .models import Profile

class NameOfUser(forms.Form):
	name = forms.CharField(label="", max_length=100)


class ChangeNicknameForm(forms.ModelForm):
	class Meta:
		model=Profile
		fields = ['nickname']


class ChangeBioForm(forms.ModelForm):
	class Meta:
		model=Profile
		fields = ['bio']