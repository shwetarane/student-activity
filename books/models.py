from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
class BookManager(models.Manager):
    def get_by_book_name(self,b_name=None):
        return super(BookManager,self)\
            .filter(book_name__contains=b_name)

    def get_by_author_name(self,a_name=None):
        return super(BookManager,self)\
            .filter(book_author=a_name)

    def get_by_isbn(self,isbn=None):
        return super(BookManager,self)\
            .filter(isbn_number=isbn)

    def get_by_b_name_and_a_name(self,b_name=None,a_name=None):
        return super(BookManager,self).get_queryset()\
            .filter(book_name=b_name,book_author=a_name)

    def get_by_b_name_and_isbn(self,b_name=None,isbn=None):
        return super(BookManager,self).get_queryset()\
            .filter(book_name=b_name,isbn_number=isbn)

    def get_by_a_name_and_isbn(self,a_name=None,isbn=None):
        return super(BookManager,self).get_queryset()\
            .filter(book_author=a_name,isbn_number=isbn)

    def get_by_all_values(self,a_name=None,isbn=None,b_name=None):
        return super(BookManager,self).get_queryset()\
            .filter(book_author=a_name,isbn_number=isbn,book_name=b_name)


class Book(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    book_name = models.CharField(max_length=30, blank=False)
    book_author = models.CharField(max_length=30, blank=False)
    published_date = models.DateField(default=timezone.now)
    book_description = models.TextField(    blank=False,null=False)
    publisher = models.CharField(max_length=30, blank=False)
    num_pages = models.IntegerField(blank=False)
    isbn_number = models.CharField(max_length=10,blank=False)
    image = models.ImageField(default='default_book.jpg',upload_to='books_pictures')
    quantity = models.IntegerField(blank=False)
    available_in_library = models.BooleanField(default=True,null=False)
    library_shelf = models.CharField(max_length=4,blank=True,null=False)
    book_store = models.CharField(max_length=60,blank=True, null=False)
    slug = models.SlugField(max_length=80,default='',null=True,blank=True, \
        help_text="This field will get filled automatically. Pleaese leave it blank")
    price =models.DecimalField(max_digits=10, decimal_places=2)

    objects = models.Manager()
    bmanager_obj  = BookManager()

    def __str__(self):
        return f'{self.book_name, self.book_author}'

    def _get_unique_slug(self):
        slug = slugify(self.book_name)
        unique_slug = slug
        num = 1
        while Book.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug,num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super(Book,self).save(*args, **kwargs)

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
        
    def get_absolute_url(self):
        return reverse('books:book_lists',
                args=[self.slug])
