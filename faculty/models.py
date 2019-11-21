from django.db import models
from PIL import Image

# Create your models here.

class Faculty(models.Model):
    faculty_fname = models.CharField(max_length=30, blank=False)
    faculty_lname = models.CharField(max_length=30, blank=False)
    faculty_department = models.CharField(max_length=20,null=False,blank=False)
    faculty_email = models.EmailField(max_length=70,blank=True)
    faculty_phoneno = models.CharField(max_length=10)
    image = models.ImageField(default='default1.jpg',upload_to='faculty_profile_picture')

    objects = models.Manager()

    def __str__(self):
        return f'{self.faculty_fname, self.faculty_lname}'
    
    def save(self, *args, **kwargs):
        super(Faculty, self).save(*args, **kwargs)
        img = Image.open(self.image.path)
        
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)