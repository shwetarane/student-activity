from django.shortcuts import render
from .models import Ticket
from cart.forms import CartAddProductForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def get_tickets(request):

    tickets = Ticket.objects.all()
    cart_form = CartAddProductForm()
    return render(request, 'bus/list.html',\
        {
            'tickets':tickets,
            'cart_form':cart_form,
        }
        )

