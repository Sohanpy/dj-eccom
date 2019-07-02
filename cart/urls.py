from django.urls import path

from .views import carthome , cart_update

app_name = 'cart'

urlpatterns = [
    path('' , carthome , name = 'details'),
    path('update' , cart_update , name = 'update')
]