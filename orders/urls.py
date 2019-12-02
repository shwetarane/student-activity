from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [

    path('create/',views.order_create,name='order_create'),
    path('history/',views.orders_history,name='orders_history'),
    path('bus_order_create/',views.bus_order_create,name='bus_order_create'),
    path('bus_history/',views.bus_orders_history,name='bus_orders_history'),
    path('meal_order_create/',views.meal_order_create,name='meal_order_create'),
    path('meal_order_history/',views.meal_orders_history,name='meal_orders_history'),
]