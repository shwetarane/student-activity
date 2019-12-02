from django.shortcuts import render, redirect, get_object_or_404
import braintree
from orders.models import Orders,BusOrders, MealOrders
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def payment_process(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Orders, id=order_id)

    if request.method == 'POST':
        nonce = request.POST.get('payment_method_nonce',None)
        result = braintree.Transaction.sale({
                'amount':'{:.2f}'.format(order.get_total_cost()),
                'payment_method_nonce' : nonce,
                'options':{
                    'submit_for_settlement':True
                }
        })
        if result.is_success:
            order.paid = True
            order.braintree_id = result.transaction.id
            order.save()
            return redirect('payment:done')
        else:
            return redirect('payment:cancelled')
    else:
        client_token = braintree.ClientToken.generate()
        return render(request,'payment/process.html',
                {'order':order,
                'client_token':client_token})

@login_required
def bus_payment_process(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(BusOrders, id=order_id)
    if request.method == 'POST':
        nonce = request.POST.get('payment_method_nonce',None)
        result = braintree.Transaction.sale({
                'amount':'{:.2f}'.format(order.get_total_cost()),
                'payment_method_nonce' : nonce,
                'options':{
                    'submit_for_settlement':True
                }
        })
        if result.is_success:
            order.paid = True
            order.braintree_id = result.transaction.id
            order.save()
            return redirect('payment:done')
        else:
            return redirect('payment:cancelled')
    else:
        client_token = braintree.ClientToken.generate()
        return render(request,'payment/process.html',
                {'order':order,
                'client_token':client_token})

@login_required
def meal_payment_process(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(MealOrders, id=order_id)
    if request.method == 'POST':
        nonce = request.POST.get('payment_method_nonce',None)
        result = braintree.Transaction.sale({
                'amount':'{:.2f}'.format(order.get_total_cost()),
                'payment_method_nonce' : nonce,
                'options':{
                    'submit_for_settlement':True
                }
        })
        print ("reults ", result)
        if result.is_success:
            order.paid = True
            order.braintree_id = result.transaction.id
            order.save()
            return redirect('payment:done')
        else:
            return redirect('payment:cancelled')
    else:
        client_token = braintree.ClientToken.generate()
        return render(request,'payment/process.html',
                {'order':order,
                'client_token':client_token})


@login_required
def payment_done(request):
    return render(request,'payment/done.html')

@login_required
def payment_canceled(request):
    return render(request,'payment/cancelled.html')
