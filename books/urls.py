from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('',views.book_list,name='book_lists'),
    path('id/<slug:slug>/',views.book_detail,name='book_details'),
    path('search/',views.book_search,name='book_search'),
]