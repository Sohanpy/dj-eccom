from django.shortcuts import render , redirect
from products.models import Products
from .models import Cart

def carthome(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    products = Cart.objects.all()

    context = {
        'cart' : cart_obj,
        'products':products
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