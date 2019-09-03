from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length = 100)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	# cascade delete - delete posts if user is deleted. 
	# will SQL statement -> python manage.py sqlmigrate blog 0001
	# python manage.py shell -> for interactive shell
	author = models.ForeignKey(User, on_delete = models.CASCADE)

	def __str__(self):
		return self.title

	# redirect - redirect to specific route
	# reverse - returns string of url to specific route
	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk':self.pk})
