import os
import random
from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save
from django.shortcuts import reverse

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

from eccommerce.utils import unique_slug_generator


def get_filename_ext(filepath):
    basename = os.path.basename(filepath)
    name , ext = os.path.splitext(basename)
    return name , ext

def upload_image_path(instance , filename):
    new_filename = random.randint(1,7075478955136)
    name , ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename = new_filename , ext=ext)
    return 'products/{new_filename}/{final_filename}'.format(
        new_filename = new_filename,
        final_filename = final_filename
    )

class Products(models.Model):
    title = models.CharField(max_length = 50)
    slug = models.SlugField(unique = True , blank = True)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2 , max_digits=20 , default = 10.99)
    image = models.ImageField(upload_to = upload_image_path , null = True)
    avatar = ImageSpecField(source='image',
                                processors=[ResizeToFill(700, 400)],
                                format='JPEG',
                                options={'quality': 60}
                            )


    featured = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def get_absolute_url(self):
        return reverse('products:detail' , kwargs={
            'slug' : self.slug
        })

def unique_slug_generator_reciever(instance , sender , *args , **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
pre_save.connect(unique_slug_generator_reciever , sender=Products)
