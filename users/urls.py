from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('search/',views.search_student,name='student_search'),
]
