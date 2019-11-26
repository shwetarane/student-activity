from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [

    path('create/',views.order_create,name='order_create'),
    path('history/',views.orders_history,name='orders_history')
]