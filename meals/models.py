from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class MealPlan(models.Model):

    plan_type = models.CharField(max_length=40)
    description = models.CharField(max_length=100)
    slug = models.SlugField(max_length=80, default='',null=True,blank=True, \
        help_text = "This field will get filled automatically")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f'{self.plan_type}'

    def _get_unique_slug(self):
        slug = slugify(self.plan_type)
        unique_slug = slug
        num = 1
        while MealPlan.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug,num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super(MealPlan,self).save(*args, **kwargs)
        
    def get_absolute_url(self):
        return reverse('eals:',
                args=[self.slug])
