from django.conf import settings
from django.shortcuts import render

from product.services import get_products


def product_list(request):
    context = {
        "products": get_products(),
        "shop_name": settings.SHOP_NAME,
        "shop_header_info": settings.SHOP_HEADER_INFO
    }

    return render(request, 'product/product_list.html', context)
