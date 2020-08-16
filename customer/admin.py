from django.contrib import admin
from django.contrib.admin import ModelAdmin

from customer.models import Customer


class CustomerAdmin(ModelAdmin):
    list_display = ('full_name', 'phone_number', 'city', 'region', 'address', 'product_price', 'product', 'created_at')


admin.site.register(Customer, CustomerAdmin)
