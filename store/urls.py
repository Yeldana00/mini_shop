from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from product.views import product_list

urlpatterns = [
    path('', product_list),
    path('epanel/', admin.site.urls)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
