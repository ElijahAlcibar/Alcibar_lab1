from django import forms

class NameOfUser(forms.Form):
	name = forms.CharField(max_length=100)
