from django.urls import path
from .views import UserListView
from . import views

app_name = 'users'

urlpatterns = [
    path('search/',views.search_student,name='student_search'),
    path('all-users/', UserListView.as_view(), name = 'all-users'),
    path('roommatesearch/',views.roommateFind,name='roommateFind'),
]
