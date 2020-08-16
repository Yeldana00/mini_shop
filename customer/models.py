from django.db import models

from product.models import Product


class Review(models.Model):
    """ Клиенттердің пікірлерін сақтауға арналған. Кейін сайтта көресету үшін. """
    text = models.TextField()
    image = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "reviews"
        verbose_name_plural = "Пікірлер"


class Customer(models.Model):
    """ Сатып алушы туралы ақпараттар """

    full_name = models.CharField(max_length=255)
    phone_number = models.PositiveIntegerField()
    city = models.CharField(max_length=255, default=None)
    region = models.CharField(max_length=255, default=None)
    address = models.TextField()
    product_price = models.IntegerField()
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "customers"
        verbose_name_plural = "Клинттер"
