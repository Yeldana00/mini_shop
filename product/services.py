from product.models import Product


def get_products():
    """ Барлық жарияланған тауарларды алу """
    return Product.objects.filter(is_published=True)