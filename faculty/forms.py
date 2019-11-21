from django import forms
from .models import Faculty


department_choices = [
		('','None'),
		('Computer Science','Computer Science'),
		('Mechanical Engineering','Mechanical Engineering'),
		('Biotechnology','Biotechnology'),
		('Civil Engineering','Civil Engineering'),
		('Aerospace','Aerospace'),
		('Chemical Engineering','Chemical Engineering')
	]

class SearchForm(forms.Form):
	first_name = forms.CharField(max_length=30,required=False)
	last_name = forms.CharField(max_length=30,required=False)
	department = forms.CharField(required=False,label='Select the department name',
			widget=forms.Select(choices=department_choices))
	
