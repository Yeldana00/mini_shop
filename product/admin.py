from django.contrib import admin
from django.contrib.admin import ModelAdmin

from product.models import Product


class AdminProduct(ModelAdmin):
    list_display = ('name', 'price')





admin.site.register(Product, AdminProduct)

