from django.db import models
from django.contrib.auth.models import User
from books.models import Book
from bus.models import Ticket
from meals.models import MealPlan

# Create your models here.
class Orders(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=15)
    city = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    braintree_id = models.CharField(max_length=160,blank=True)
    total_price = models.DecimalField(max_digits=10,decimal_places=2,default=0)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())    
        
class OrderItem(models.Model):
    
    user = models.ForeignKey(User, related_name='ordered_users',\
                                on_delete=models.CASCADE)
    order = models.ForeignKey(Orders,related_name='items',
                                on_delete=models.CASCADE)
    book = models.ForeignKey(Book,related_name='order_books',
                                on_delete=models.CASCADE)

    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity


# Bus Ticket Details

class BusOrders(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=15)
    city = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    braintree_id = models.CharField(max_length=160,blank=True)
    total_price = models.DecimalField(max_digits=10,decimal_places=2,default=0)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())    

class BusOrderItem(models.Model):
    
    user = models.ForeignKey(User, related_name='bus_ordered_users',\
                                on_delete=models.CASCADE)
    order = models.ForeignKey(BusOrders,related_name='items',
                                on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket,related_name='order_books',
                                on_delete=models.CASCADE)

    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity


# Meal Plan Models

class MealOrders(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=15)
    city = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    braintree_id = models.CharField(max_length=160,blank=True)
    total_price = models.DecimalField(max_digits=10,decimal_places=2,default=0)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())    

class MealOrderItem(models.Model):
    
    user = models.ForeignKey(User, related_name='meal_ordered_users',\
                                on_delete=models.CASCADE)
    order = models.ForeignKey(MealOrders,related_name='items',
                                on_delete=models.CASCADE)
    meal = models.ForeignKey(MealPlan,related_name='order_meal',
                                on_delete=models.CASCADE)

    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity