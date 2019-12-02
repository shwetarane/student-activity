from django.urls import path
from . import views

app_name = 'meals'

urlpatterns = [
    path('',views.get_meals,name='get_meals'),
]