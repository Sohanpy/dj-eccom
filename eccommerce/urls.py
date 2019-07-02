from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include('products.urls' , namespace= 'products')),
    path('accounts/' , include('accounts.urls' , namespace= 'accounts')),
    path('cart/' , include('cart.urls' , namespace= 'cart'))

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)