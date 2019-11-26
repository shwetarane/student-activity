from django import forms
from .models import Orders

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Orders
        
        fields = ['first_name','last_name','email',
                'address','postal_code','city']
        

                