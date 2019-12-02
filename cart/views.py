from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.conf import settings
from books.models import Book
from bus.models import Ticket
from .cart import Cart
from .forms import CartAddProductForm
from orders.models import Orders
from meals.models import MealPlan


# Create your views here.
@login_required
@require_POST
def cart_add(request, book_id):
    cart = Cart(request,'cart')
    book = get_object_or_404(Book,id=book_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cl_data = form.cleaned_data
        cart.add(book_obj=book,
                quantity=cl_data['quantity'],
                update_quantity=cl_data['update'])
       
    return redirect('cart:cart_detail')

@login_required
def cart_remove(request,book_id):
    cart = Cart(request,'cart')
    book = get_object_or_404(Book,id=book_id)
    cart.remove(book)
    return redirect('cart:cart_detail')

@login_required
def cart_detail(request):
    cart = Cart(request,'cart')
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(\
            initial={'quantity':item['quantity'],
            'update':True})
    return render(request, 'cart/detail.html',
                {'cart':cart})

@login_required
def cart_ticket_detail(request):
    cart = Cart(request,'cart')
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(\
            initial={'quantity':item['quantity'],
            'update':True})
    return render(request, 'cart/ticket_detail.html',
                {'cart':cart})
@login_required
def cart_add_ticket(request, ticket_id):
    cart = Cart(request,'ticket')
    book = get_object_or_404(Ticket,id=ticket_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cl_data = form.cleaned_data
        cart.add(book_obj=book,
                quantity=cl_data['quantity'],
                update_quantity=cl_data['update'])
       
    return redirect('cart:ticket_cart_detail')


@login_required
def cart_remove_ticket(request,ticket_id):
    cart = Cart(request,'ticket')
    book = get_object_or_404(Ticket,id=ticket_id)
    cart.remove(book)
    return redirect('cart:ticket_cart_detail')

@login_required
def cart_detail_ticket(request):
    
    cart = Cart(request,'ticket')
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(\
            initial={'quantity':item['quantity'],
            'update':True})
    return render(request, 'cart/ticket_detail.html',
                {'cart':cart,
                })

# Meals Cart 

@login_required
def cart_add_meal(request, meal_id):
    cart = Cart(request,'meal')
    book = get_object_or_404(MealPlan,id=meal_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cl_data = form.cleaned_data
        cart.add(book_obj=book,
                quantity=cl_data['quantity'],
                update_quantity=cl_data['update'])
       
    return redirect('cart:cart_detail_meal')

@login_required
def cart_remove_meal(request,meal_id):
    cart = Cart(request,'meal')
    book = get_object_or_404(MealPlan,id=meal_id)
    cart.remove(book)
    return redirect('cart:cart_detail_meal')

@login_required
def cart_detail_meal(request):
    
    cart = Cart(request,'meal')
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(\
            initial={'quantity':item['quantity'],
            'update':True})
    return render(request, 'cart/meal_detail.html',
                {'cart':cart,
                })



