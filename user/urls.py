from django.urls import path
from user import views

app_name = 'user'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('user_name/', views.user_name, name='user_name'),
    path('get_captcha/', views.get_captcha, name="get_captcha"),
    path('register_ok/', views.register_ok, name="register_ok"),
    path('exit/', views.exit, name="exit"),
]
