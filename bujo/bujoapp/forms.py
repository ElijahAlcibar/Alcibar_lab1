from django import forms

from .models import ProfilePageModel

class NameOfUser(forms.Form):
	name = forms.CharField(label="", max_length=100)


class NicknameProfileForm(forms.ModelForm):
	class Meta:
		model = ProfilePageModel
		fields = ['nickname']
