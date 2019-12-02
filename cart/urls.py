from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('',views.cart_detail,name='cart_detail'),
    path('add/<int:book_id>/',views.cart_add,name='cart_add'),
    path('remove/<int:book_id>/',views.cart_remove,name='cart_remove'),
    path('ticket/<int:ticket_id>/',views.cart_add_ticket,name='cart_add_ticket'),
    path('ticket_cart/',views.cart_detail_ticket,name='ticket_cart_detail'),
    path('ticket_cart_remove/<int:ticket_id>/',views.cart_remove_ticket,name='ticket_cart_remove'),
    path('meal_cart/<int:meal_id>/',views.cart_add_meal,name='cart_add_meal'),
    path('meal_cart_detail/',views.cart_detail_meal,name='cart_detail_meal'),
    path('meal_cart_remove/<int:meal_id>/',views.cart_remove_meal,name='cart_remove_meal'),
]