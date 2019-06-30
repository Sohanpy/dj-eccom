from django.urls import path

from . views import HomePageView , ProductDetailView

app_name = 'products'

urlpatterns = [
    path('' , HomePageView.as_view() , name = 'home'),
    path('detail/<slug>/' , ProductDetailView.as_view() , name = 'detail'),
]