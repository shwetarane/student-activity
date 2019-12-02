from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import MealPlan
from cart.forms import CartAddProductForm

# Create your views here.
@login_required
def get_meals(request):

    meals_list = MealPlan.objects.all()
    cart_form = CartAddProductForm()
    return render(request, 'meals/list.html',\
        {
            'meals_list':meals_list,
            'cart_form':cart_form,
        }
        )