from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=30, blank=True)
    city = models.CharField(max_length=30, blank=True)
    state = models.CharField(max_length=30, blank=True)
    zip_code = models.IntegerField(default=78758)
    birth_date = models.DateField(null=True, blank=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pictures')

    def __str__(self):
    	return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
    	super(UserProfile, self).save(*args, **kwargs)

    	img = Image.open(self.image.path)
    	
    	if img.height > 300 or img.width > 300:
    		output_size = (300, 300)
    		img.thumbnail(output_size)
    		img.save(self.image.path)