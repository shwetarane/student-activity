from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin,  UserPassesTestMixin
from django.views.generic import (
	ListView, 
	DetailView, 
	CreateView,
	UpdateView,
	DeleteView,
	)
from .models import Post


# Create your views here.
def home(request):
	context = {
		'posts' : Post.objects.all()
	}
	return render(request, 'blog/home.html', context)

class PostListView(ListView):
	model = Post
	template_name = 'blog/home.html' #<app>/<model>_<viewtype>.html
	context_object_name = 'posts'
	ordering = ['-date_posted']


class PostDetailView(DetailView):
	model = Post
	# template_name = 'blog/post_detail.html'


class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['title', 'content']
	# template_name = 'blog/post_form.html'

	# before you submit the form set the user to current logged in user
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	success_url = '/'
	
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
		    return True
		return False


def about(request):
	return render(request, 'blog/about.html', {'title':'About'})