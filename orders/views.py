from django.shortcuts import render,redirect, reverse
from .models import OrderItem, Orders, BusOrderItem, MealOrderItem
from .forms import OrderCreateForm, BusOrderCreateForm, MealOrderCreateForm
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


@login_required
def meal_order_create(request):
    cart = Cart(request,'meal')
    if request.method == 'POST':
        form = MealOrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            total_price = 0
            total_price_a =0
            for item in cart:
                if item['book'].plan_type == 'Semester Plan':
                    total_price_a += item['price'] * item['quantity']
                    total_price_a = total_price_a - (total_price_a * Decimal(.05))
                    MealOrderItem.objects.create(user=request.user,
                                    order=order,
                                    meal=item['book'],
                                    price=total_price_a,
                                    quantity=item['quantity'])
                else:
                    total_price += item['price'] * item['quantity']
                    MealOrderItem.objects.create(user=request.user,
                                    order=order,
                                    meal=item['book'],
                                    price=item['price'],
                                    quantity=item['quantity'])

            total_price+=total_price_a
            #order.total_price = cart.get_ticket_price()
            order.total_price = total_price
            order = form.save()
            cart.meal_cart_clear()
            request.session['order_id'] = order.id
            return redirect(reverse('payment:meal_payment_process'))
            #return render(request,'orders/created.html',
            #           {'order':order})
    else:
        form = MealOrderCreateForm()
    return render(request,'orders/meal_order_create.html',
                    {'cart':cart,'form':form})

@login_required
def meal_orders_history(request):

    orders = MealOrderItem.objects.filter(user=request.user)
    
    paginator = Paginator(orders,10)
    page = request.GET.get('page')
    try:
        orders = paginator.page(page)
    except PageNotAnInteger:
        orders = paginator.page(1)
    except EmptyPage:
        orders = paginator.page(paginator.num_pages)
    return render(request, 'orders/meals.html',\
            {
                'orders':orders
            })