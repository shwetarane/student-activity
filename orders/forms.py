from django import forms
from .models import Orders, BusOrders, MealOrders

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Orders
        
        fields = ['first_name','last_name','email',
                'address','postal_code','city']

class BusOrderCreateForm(forms.ModelForm):
    class Meta:
        model = BusOrders
        
        fields = ['first_name','last_name','email',
                'address','postal_code','city']

class MealOrderCreateForm(forms.ModelForm):
    class Meta:
        model = MealOrders
        
        fields = ['first_name','last_name','email',
                'address','postal_code','city']
        

                