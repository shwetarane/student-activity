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
]