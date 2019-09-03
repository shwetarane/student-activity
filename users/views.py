from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import SignUpForm, UserProfileForm, UserUpdateForm, UserProfileUpdateForm

def index(request):
	if request.user.is_authenticated:
		username = request.user.username
	else:
		username = 'Not Logged In'

	context = {'username' : username}
	return render(request, 'blog-home', context)

def register(request):
    # try:
    #     profile = request.user.UserProfileForm
    # except UserProfile.DoesNotExist:
    #     profile = UserProfile(user = request.user)

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if form.is_valid() and profile_form.is_valid():
            user = form.save()

            profile = profile_form.save(commit = False)
            profile.user = user

            # profile.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=password)
            login(request, user)
            messages.success(request, f'Account created. You will now be able to login in {username}!')
            return redirect('login')
    else:
        form = SignUpForm()
        profile_form = UserProfileForm()

    context = {'form' : form, 'profile_form' : profile_form}
    return render(request, 'users/register.html', context)


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance = request.user)
        p_form = UserProfileUpdateForm(request.POST, 
                                       request.FILES, 
                                       instance = request.user.userprofile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Account Information updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance = request.user)
        p_form = UserProfileUpdateForm(instance = request.user.userprofile)
    
    context={
        'u_form' : u_form, 
        'p_form' : p_form
    }
    return render(request, 'users/profile.html', context)




