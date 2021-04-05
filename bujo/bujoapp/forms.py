from django import forms

class NameOfUser(forms.Form):
	name = forms.CharField(label="", max_length=100)
