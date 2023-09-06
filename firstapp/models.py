from django.db import models
from django.utils.html import mark_safe


class Order(models.Model):
    order_dt = models.DateTimeField(auto_now=True)
    order_name = models.CharField(max_length=200)
    order_phone = models.CharField(max_length=200)
    order_img = models.ImageField()


class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products/')
    description = models.TextField()
    price = models.DecimalField(max_digits=100_000_000, decimal_places=0)

    def image_tag(self):
        return mark_safe(f'<img src="{self.image.url}" width="50" height="50" />')

    image_tag.short_description = 'Image'

    def __str__(self):
        return self.name


