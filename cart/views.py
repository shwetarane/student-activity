from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from books.models import Book
from .cart import Cart
from .forms import CartAddProductForm
from orders.models import Orders

# Create your views here.
@login_required
@require_POST
def cart_add(request, book_id):
    cart = Cart(request)
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
    cart = Cart(request)
    book = get_object_or_404(Book,id=book_id)
    cart.remove(book)
    return redirect('cart:cart_detail')

@login_required
def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(\
            initial={'quantity':item['quantity'],
            'update':True})
    return render(request, 'cart/detail.html',
                {'cart':cart})

