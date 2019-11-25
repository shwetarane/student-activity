from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, get_list_or_404
from .models import UserProfile
from .forms import SignUpForm, UserProfileForm, UserUpdateForm, \
    UserProfileUpdateForm, SearchForm
from django.views.generic import ListView
from django.http.response import Http404

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

            #profile.save()

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

def userhome(request):
    context = {
    'users' : UserProfile.objects.all()
    }
    print(context)
    return render (request, 'users/allusers.html', context)

class UserListView(ListView):
    model = UserProfile
    template_name = 'users/allusers.html'
    context_object_name = 'users'

@login_required
def search_student(request):
    '''
    Seach the students by first_name, last_name and department
    '''

    form = SearchForm()
    f_name = l_name = dept = None
    results = []
    # Need to validate in a different way
    if 'first_name' in request.GET:
        form = SearchForm(request.GET)
        form.full_clean()

        if form.cleaned_data['first_name']!='' and form.cleaned_data['last_name']!='' \
            and form.cleaned_data['department'] != '':
            f_name = form.cleaned_data['first_name']
            l_name = form.cleaned_data['last_name']
            dept = form.cleaned_data['department']
            results = get_list_or_404(UserProfile,department=dept,\
                user__first_name=f_name,user__last_name=l_name)

        else:
            try:
                if form.cleaned_data['first_name']!='' and form.cleaned_data['last_name']!='':
                    results = get_list_or_404(UserProfile,user__first_name=\
                            form.cleaned_data['first_name'],
                            user__last_name=form.cleaned_data['last_name'])
                elif form.cleaned_data['first_name']!='' and form.cleaned_data['department']!='':
                    results = get_list_or_404(UserProfile,user__first_name=\
                            form.cleaned_data['first_name'],
                            department=form.cleaned_data['department'])
                elif form.cleaned_data['last_name']!='' and form.cleaned_data['department']!='':
                    results = get_list_or_404(UserProfile,user__last_name=\
                            form.cleaned_data['last_name'],
                            department=form.cleaned_data['department'])
                elif form.cleaned_data['first_name']!='' and form.cleaned_data['last_name']=='' and\
                    form.cleaned_data['department']=='':
                    results = get_list_or_404(UserProfile,user__first_name=\
                            form.cleaned_data['first_name'])
                elif form.cleaned_data['last_name']!='' and form.cleaned_data['department']=='' and \
                    form.cleaned_data['first_name']=='':
                    results = get_list_or_404(UserProfile,user__last_name=\
                            form.cleaned_data['last_name'])
                elif form.cleaned_data['department']!='' and form.cleaned_data['first_name']=='' and\
                    form.cleaned_data['last_name']=='':
                    results = get_list_or_404(UserProfile,
                            department=form.cleaned_data['department'])
            except Http404:
                raise Http404("No match is availabe for the given query %s %s %s" \
                    %(form.cleaned_data['first_name'],form.cleaned_data['last_name'],\
                        form.cleaned_data['department']))

            print(results)
    return render(request,'users/search.html',{'form':form,\
            'results':results})
