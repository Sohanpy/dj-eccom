from django.shortcuts import render
from django.views.generic import ListView , DetailView

from .models import Products

class HomePageView(ListView):
    model = Products
    template_name = 'index.html'
    context_object_name = 'products'
    paginate_by = 9


class ProductDetailView(DetailView):
    model = Products
    template_name = 'details.html'
    context_object_name = 'object'
