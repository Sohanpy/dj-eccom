from django.shortcuts import render , redirect
from products.models import Products
from orders.models import Oder
from accounts.forms import GuestForm
from .models import Cart



def carthome(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    products = Cart.objects.all()
    order = Oder.objects.all()

    context = {
        'cart' : cart_obj,
        'products':products,
    }
    return render(request , 'cart.html' , context)

def cart_update(request):
    product_id = request.POST.get('product_id')
    if product_id is not None:
        try:
            product_obj = Products.objects.get(id = product_id)
        except Products.DoesNotExist:
            print('error, product does not exists')
            return redirect('/')

        cart_obj , new_obj = Cart.objects.new_or_get(request)
        if product_obj in cart_obj.products.all():
            cart_obj.products.remove(product_obj)
        else:
            cart_obj.products.add(product_obj)
        request.session['total_item'] = cart_obj.products.count()
    return redirect('cart:details')

def checkout_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    order_obj = None
    if new_obj or cart_obj.products.count() ==0:
        return redirect('cart:details')
    else:
        order_obj , new_order_obj = Oder.objects.get_or_create(cart = cart_obj)

    context = {
        'object':order_obj
    }
    return render(request , 'checkout.html' , context)