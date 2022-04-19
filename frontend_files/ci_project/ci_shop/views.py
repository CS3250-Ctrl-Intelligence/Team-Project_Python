from itertools import product
from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from ci_shop.models import Product

from ci_cart.models import CartItem, Cart
from ci_cart.views import _cart_session


def shop(request):
    # Query all products in database where in_stock is True
    products = Product.objects.all().filter(in_stock=True).order_by('id')
    # Implement paginator separate the amount of product available for view each page
    paginator = Paginator(products, 10)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)

    product_count = products.count()
    # check to see if the product is already in cart

    context = {
        'products': paged_products,
        'product_count': product_count,

    }
    return render(request, 'shop.html', context)


def product_detail(request, product_slug,):
    # category__slug means the slug attribute of category
    try:
        product_detail = Product.objects.get(slug=product_slug)
        related_products = Product.objects.filter(supplier_id=product_detail.supplier_id).exclude(slug=product_detail.slug)[:4]

        # check to see if the product is already in cart
        if request.user.is_authenticated:
            in_cart = CartItem.objects.filter(user=request.user, product=product_detail)
        else:
            in_cart = CartItem.objects.filter(cart__cart_id=_cart_session(request)).exists()
    except Exception as e:
        raise e

    return render(request, 'productDetail.html',
                  {'product_detail': product_detail, 'in_cart': in_cart, 'related': related_products, })
