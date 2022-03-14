
from itertools import product
from django.shortcuts import get_object_or_404, render
from ci_shop.models import Product
from ci_category.models import Category
from ci_cart.models import CartItem,Cart

from ci_cart.views import _cart_session
# Create your views here.


def shop(request,category_slug=None):
    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug = category_slug )
        products = Product.objects.all().filter(category = categories, in_stock = True)
        # count number of products, not quantity of each
        product_count = products.count()
    else:
        products = Product.objects.all().filter(in_stock = True)
        product_count = products.count()

    return render(request, 'shop.html', {'products':products,'product_count':product_count})

def product_detail(request,category_slug, product_slug):
    #category__slug means the slug attribute of category
    try:
        product_detail= Product.objects.get(category__slug= category_slug ,slug = product_slug)

        # check to see if the product is already in cart
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_session(request)).exists()
    except Exception as e:
        raise e
    return render(request,'productDetail.html',{'product_detail':product_detail,'in_cart':in_cart,})

