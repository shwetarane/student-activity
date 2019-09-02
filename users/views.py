from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.
def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		# checks for user_input validation
		if form.is_valid():
			# save user if form data is valid
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account created {username}')
			return redirect('blog-home')
	else:
		form = UserRegisterForm()
	return render(request, "users/register.html", {'form': form})


# messages.debug
# messages.warning
# messages.success
# messages.error