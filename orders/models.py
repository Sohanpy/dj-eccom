import math
from django.db import models
from django.db.models.signals import pre_save , post_save

from eccommerce.utils import unique_order_id_generator

from cart.models import Cart

ORDER_STATUS = (
    ('created' , 'Created'),
    ('paid' , 'Paid')
)


class Oder(models.Model):
    order_id = models.CharField(max_length = 45 , blank = True)
    cart = models.ForeignKey(Cart , on_delete = models.CASCADE)
    status = models.CharField(choices = ORDER_STATUS , blank = True, max_length = 20)
    shipping_total = models.DecimalField(default = 5.99 , max_digits= 25 , decimal_places=2)
    total = models.DecimalField(default = 5.99 , max_digits= 25 , decimal_places=2)

    def __str__(self):
        return self.order_id

    def update_total(self):
        cart_total = self.cart.total
        shipping_total = self.shipping_total
        new_total = math.fsum([cart_total , shipping_total])
        formatted_total = format(new_total , '.2f')
        self.total = formatted_total
        self.save()
        return new_total


def order_id_genaretor_reciever(sender , instance , *args , **kwargs):
    if not instance.order_id:
        instance.order_id = unique_order_id_generator(instance)

pre_save.connect(order_id_genaretor_reciever , sender=Oder)


def post_save_cart_total(sender , instance ,created , *args , **kwargs):
    if not created:
        cart_obj = instance
        cart_id = cart_obj.id
        cart_total = cart_obj.total
        qs = Oder.objects.filter(cart__id = cart_id)
        if qs.count() == 1:
            order_obj = qs.first()
            order_obj.update_total()

post_save.connect(post_save_cart_total , sender=Cart)

def post_save_cart_total_new(sender , instance ,created , *args , **kwargs):
    if created:
        instance.update_total()
post_save.connect(post_save_cart_total_new , sender=Oder)
