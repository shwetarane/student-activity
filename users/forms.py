from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile

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
		fields = ('address','city','state','zip_code', 'birth_date','image', )