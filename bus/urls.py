from django.urls import path
from . import views

app_name = 'bus'

urlpatterns = [
    path('',views.get_tickets,name='get_tickets'),
]