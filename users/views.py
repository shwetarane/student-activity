from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import SignUpForm, UserProfileForm

def index(request):
	if request.user.is_authenticated:
		username = request.user.username
	else:
		username = 'Not Logged In'

	context = {'username' : username}
	return render(request, 'blog-home', context)

@login_required
def profile(request):
	return render(request, 'users/profile.html', context)

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if form.is_valid() and profile_form.is_valid():
            user = form.save()

            profile = profile_form.save(commit = False)
            profile.user = user

            profile.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=password)
            login(request, user)

            return redirect('blog-home')
    else:
        form = SignUpForm()
        profile_form = UserProfileForm()

    context = {'form' : form, 'profile_form' : profile_form}
    return render(request, 'users/register.html', context)

