from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile


role_choices = [
		('students','Students'),
		('professor','Professor'),
	]
department_choices = [
		('','None'),
		('computer science','Computer Science'),
		('Mechnical Engineering','Mechanical Engineering'),
		('biotechnology','Biotechnology'),
		('civilengineering','Civil Engineering'),
		('aerospace','Aerospace'),
		('chemicalengineering','Chemical Engineering')
	]

gender_choices = [ ('', 'None'), ('Male','MALE'),
				   ('Female','FEMALE')]

class SignUpForm(UserCreationForm):
	email = forms.EmailField()
	first_name = forms.CharField()
	last_name = forms.CharField()

	class Meta:
		model = User
		fields = ('username', 'email', 'first_name', 'last_name','password1', 'password2', )

	def save(self, commit=True):
		user=super().save(commit=False)

		user.email = self.cleaned_data['email']
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']

		if commit:
			user.save()
		return user

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('birth_date', 'address', 'city', 'state', 'zip_code')

# to update username and email
class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()
	class Meta:
		model = User
		fields = ('username', 'email',)

# #to update avatar
class UserProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('address','city','state','zip_code', 'birth_date','image','department')

class SearchForm(forms.Form):
	first_name = forms.CharField(max_length=30,required=False)
	last_name = forms.CharField(max_length=30,required=False)
	department = forms.CharField(required=False,label='Select the department name',
			widget=forms.Select(choices=department_choices))

class RoommateSearchForm(forms.Form):
	gender = forms.CharField ( required=False, label='Gender',
							   widget=forms.Select ( choices=gender_choices ))
	from_date = forms.DateField (label='Move in Date', widget=forms.SelectDateWidget)
	to_date = forms.DateField (label='Move out Date', widget=forms.SelectDateWidget)
	price = forms.DecimalField(label='Price Within')
