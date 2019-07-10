from django.urls import path
from .views import login_page , register_page , guest_register_view

app_name = 'accounts'

urlpatterns = [
    path('login' , login_page , name = 'login'),
    path('register' , register_page , name = 'register'),
    path('guest_register' , guest_register_view , name = 'guest-register')
]