from django.contrib import admin
from .models import Order
from .models import Product


admin.site.register(Order)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'image_tag')


admin.site.register(Product, ProductAdmin)