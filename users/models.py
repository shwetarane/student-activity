from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Created by Divya
'''
class UserProfileManager(models.Manager):
    def get_department(self,dept_name=None):
        return super(UserProfileManager,self).get_queryset()\
            .filter(department=dept_name)
       
class UserManagerNew(models.Manager):
    # Modified by Divya for filtering f_name and l_name from the User model
    def get_name(self,f_name=None, l_name=None):
        return super(UserManagerNew,self).get_queryset()\
            .filter(first_name=f_name,last_name=l_name)
'''

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=30, blank=True)
    city = models.CharField(max_length=30, blank=True)
    state = models.CharField(max_length=30, blank=True)
    zip_code = models.IntegerField(default=78758)
    birth_date = models.DateField(null=True, blank=True)
    department = models.CharField(max_length=20,null=False,blank=False)
    image = models.ImageField(default='default.jpg', upload_to='profile_pictures')

    # Computer Science manager
    objects = models.Manager()
    #comp_science = UserProfileManager() 
    def __str__(self):
    	return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
    	super(UserProfile, self).save(*args, **kwargs)

    	img = Image.open(self.image.path)
    	
    	if img.height > 300 or img.width > 300:
    		output_size = (300, 300)
    		img.thumbnail(output_size)
    		img.save(self.image.path)