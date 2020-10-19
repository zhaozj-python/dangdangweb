from django.urls import path
from index import views

app_name = 'index'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('booklist/',views.booklist,name='booklist'),
    path('book_details/',views.book_details,name='book_details'),
]