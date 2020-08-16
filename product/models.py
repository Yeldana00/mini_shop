from django.conf import settings
from django.db import models


class Product(models.Model):
    """ Бүкіл тауарлар сақталады """

    name = models.CharField("Аты", max_length=255)
    price = models.IntegerField("Бағасы", default=None)
    image = models.ImageField("Суреті", upload_to='product/images')
    position = models.IntegerField("Нешінші орналасады?")
    is_published = models.BooleanField(default=False)

    @staticmethod
    def buy_link():
        return "https://wa.me/{0}?text=Қайырлы күн. Номері: {1} тауар туралы білгім келеді.".format(
            settings.WHATSAPP_NUMBER, 1)

    class Meta:
        db_table = "products"
        verbose_name_plural = "Тауарлар"
        ordering = ['position']
