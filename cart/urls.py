from django.urls import path

from .views import carthome , cart_update , checkout_home

app_name = 'cart'

urlpatterns = [
    path('' , carthome , name = 'details'),
    path('update' , cart_update , name = 'update'),
    path('checkout' , checkout_home , name = 'checkout')
]