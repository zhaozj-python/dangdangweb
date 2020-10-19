from django.urls import path
from car import views

app_name = 'car'

urlpatterns = [
    path('car/', views.car, name='car'),
    path('order/', views.order, name='order'),
    path('order_ok/', views.order_ok, name='order_ok'),
    path('add_car/', views.add_car, name='add_car'),
    path('add/', views.add, name='add'),
    path('del_car/', views.del_car, name='del_car'),
    path('modify_book/', views.modify_book, name='modify_book'),
    path('address_1/', views.address_1, name='address_1'),
    path('buy/', views.buy, name='buy'),
]