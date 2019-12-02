from django.urls import path
from . import views

app_name = 'payment'

urlpatterns = [
    path('process/',views.payment_process,name='process'),
    path('done/',views.payment_done,name='done'),
    path('cancelled',views.payment_canceled,name='cancelled'),
    path('bus_process/',views.bus_payment_process,name='bus_payment_process'),
    path('meal_process/',views.meal_payment_process,name='meal_payment_process'),
]