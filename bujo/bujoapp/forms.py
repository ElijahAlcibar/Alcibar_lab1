from django import forms

class NameOfUser(forms.Form):
	name = forms.CharField(label="Hello! What is your name?", max_length=100)
