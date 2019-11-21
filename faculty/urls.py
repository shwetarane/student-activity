from django.urls import path
from . import views

app_name = 'faculty'

urlpatterns = [
    path('search/',views.search_faculty,name='search_faculty'),
]
