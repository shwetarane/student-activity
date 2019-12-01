from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Ticket(models.Model):
    ticket_type = models.CharField(max_length=30)
    slug = models.SlugField(max_length=50,default="",null=True, blank=True, \
                help_text="This field will get filled automatically. Pleaese leave it blank")
    source = models.CharField(max_length=30)
    destination = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=10,decimal_places=2, default=0)

    def __str__(self):
        return f'{self.ticket_type}'

    def _get_unique_slug(self):
        slug = slugify(self.ticket_type)
        unique_slug = slug
        num = 1
        while Ticket.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug,num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super(Ticket,self).save(*args, **kwargs)
        
    def get_absolute_url(self):
        return reverse('bus:',
                args=[self.slug])



'''
    user = models.ForeignKey(User,related_name='ticket_users', \
            on_delete=models.CASCADE)
    order = models.ForeignKey()

'''