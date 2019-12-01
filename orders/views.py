from django.shortcuts import render,redirect, reverse
from .models import OrderItem, Orders, BusOrderItem
from .forms import OrderCreateForm, BusOrderCreateForm
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from decimal import Decimal
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
@login_required
def order_create(request):
    cart = Cart(request,'cart')
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            total_price = 0
            for item in cart:
                OrderItem.objects.create(user=request.user,
                                    order=order,
                                    book=item['book'],
                                    price=item['price'],
                                    quantity=item['quantity'])
                total_price += item['price'] * item['quantity']
            last_order = Orders.objects.latest('created')
            if last_order:
                if last_order.total_price > 200:                
                    total_price = cart.get_total_price - (cart.get_total_price() *.10)
                else:
                    total_price = cart.get_total_price()
            else:
                total_price = cart.get_total_price()
            order.total_price = total_price
            order = form.save()
            cart.clear()
            request.session['order_id'] = order.id
            return redirect(reverse('payment:process'))
            #return render(request,'orders/created.html',
            #            {'order':order})
    else:
        form = OrderCreateForm()
    return render(request,'orders/create.html',
                    {'cart':cart,'form':form})

@login_required
def orders_history(request):

    orders = OrderItem.objects.filter(user=request.user)
    
    paginator = Paginator(orders,10)
    page = request.GET.get('page')
    try:
        orders = paginator.page(page)
    except PageNotAnInteger:
        orders = paginator.page(1)
    except EmptyPage:
        orders = paginator.page(paginator.num_pages)
    return render(request, 'orders/list.html',\
            {
                'orders':orders
            })
@login_required
def bus_order_create(request):
    cart = Cart(request,'ticket')
    if request.method == 'POST':
        form = BusOrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            total_price = 0
            for item in cart:
                BusOrderItem.objects.create(user=request.user,
                                    order=order,
                                    ticket=item['book'],
                                    price=item['price'],
                                    quantity=item['quantity'])
                total_price += item['price'] * item['quantity']
            order.total_price = cart.get_ticket_price()
            order = form.save()
            cart.bus_cart_clear()
            request.session['order_id'] = order.id
            return redirect(reverse('payment:bus_payment_process'))
            #return render(request,'orders/created.html',
            #           {'order':order})
    else:
        form = BusOrderCreateForm()
    return render(request,'orders/bus_order_create.html',
                    {'cart':cart,'form':form})

@login_required
def bus_orders_history(request):

    orders = BusOrderItem.objects.filter(user=request.user)
    
    paginator = Paginator(orders,10)
    page = request.GET.get('page')
    try:
        orders = paginator.page(page)
    except PageNotAnInteger:
        orders = paginator.page(1)
    except EmptyPage:
        orders = paginator.page(paginator.num_pages)
    return render(request, 'orders/tickets.html',\
            {
                'orders':orders
            })