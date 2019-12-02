from decimal import Decimal
from django.conf import settings
from books.models import Book
from orders.models import Orders
from bus.models import Ticket
from meals.models import MealPlan
import decimal

class Cart(object):

    def __init__(self,request,session_id):
        self.session = request.session
        cart = self.session.get(session_id)
        self.which_session = session_id
        if not cart:
            # Saving an empty cart in the session #1st time
            cart = self.session[session_id] = {}
        self.cart = cart
        
    def add(self,book_obj,quantity=1,update_quantity=False):
        
        book_id = str(book_obj.id)
        if book_id not in self.cart:
            self.cart[book_id] = {'quantity':0,\
                                'price':str(book_obj.price)}
        if update_quantity:
            self.cart[book_id]['quantity'] = quantity
        else:
            self.cart[book_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session.modified = True
        
    def remove(self,book_obj):

        book_id = str(book_obj.id)
        if book_id in self.cart:
            del self.cart[book_id]
            self.save()

    def __iter__(self):

        book_ids = self.cart.keys()
        
        if self.which_session == 'cart':
            books = Book.objects.filter(id__in=book_ids)
        elif self.which_session == 'ticket':
            books = Ticket.objects.filter(id__in=book_ids)
        elif self.which_session == 'meal':
            books = MealPlan.objects.filter(id__in=book_ids)

        cart = self.cart.copy()
        for book in books:
            cart[str(book.id)]['book'] = book
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item
        
    def  __len__(self):

        return sum(item['quantity'] for item in self.cart.values())

    def get_discount(self):
        last_order = Orders.objects.latest('created')
        discount = 0
        if last_order:
            if last_order.total_price > 200:
                discount = self.get_total_price() * Decimal(.10)
                return round(discount,2)
        return round(discount,2)

    def get_discounted_price(self):
        last_order = Orders.objects.latest('created')
        if last_order:
            if last_order.total_price > 200:                
                total_price = self.get_total_price() - (self.get_total_price() * Decimal(.10))
            else:
                total_price = self.get_total_price()
        else:
            total_price = self.get_total_price()
        return round(Decimal(float(total_price)),2)


        # meal Plans

    def get_meal_discount(self):
        cart = self.cart.copy()
        total_price = 0
        for item in cart:
            if cart[item]['book'].plan_type == 'Semester Plan':
                total_price += cart[item]['price'] * cart[item]['quantity']
        discount = total_price * Decimal(.05)
        return round(discount,2)

    def get_meal_discounted_price(self):
        cart = self.cart.copy()
        total_price = 0
        total_price_a =0
        discount =0
        for item in cart:
            if cart[item]['book'].plan_type == 'Semester Plan':
                total_price_a += cart[item]['price'] * cart[item]['quantity']
                discount = total_price_a * Decimal(.05)
                total_price_a -= discount
            else:
                total_price += cart[item]['price'] * cart[item]['quantity']
        total_price += total_price_a
        return round(total_price,2)
        
    def get_total_price(self):

        return round(sum(Decimal(float(item['price']) * item['quantity']) for item in self.cart.values()),2)

    def get_ticket_price(self):
        return round(sum(Decimal(float(item['price']) * item['quantity']) for item in self.cart.values()),2)

    def clear(self):
        del self.session[self.which_session]
        self.save()

    def bus_cart_clear(self):
        del self.session[self.which_session]
        self.save()

    def meal_cart_clear(self):
        del self.session[self.which_session]
        self.save()





