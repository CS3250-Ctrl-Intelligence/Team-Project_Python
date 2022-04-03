from itertools import product
from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from ci_shop.models import Product
from ci_category.models import Category
from ci_cart.models import CartItem,Cart
from ci_cart.views import _cart_session



def shop(request,category_slug=None):
    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug = category_slug )
        products = Product.objects.all().filter(category = categories, in_stock = True)
        # Implement paginator seperate the amount of product available for view each page
        paginator = Paginator(products,4)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)

        # count number of products, not quantity of each
        product_count = products.count()
    else:
        # Query all products in database where in_stock is True
        products = Product.objects.all().filter(in_stock = True).order_by('id')
        # Implement paginator seperate the amount of product available for view each page
        paginator = Paginator(products,10)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)

        product_count = products.count()

    context={
            'products':paged_products,
            'product_count':product_count,
            }
    return render(request, 'shop.html', context)

def product_detail(request,category_slug, product_slug):
    #category__slug means the slug attribute of category
    try:
        product_detail= Product.objects.get(category__slug= category_slug ,slug = product_slug)

        # check to see if the product is already in cart
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_session(request)).exists()
    except Exception as e:
        raise e
    return render(request,'productDetail.html',{'product_detail':product_detail,'in_cart':in_cart,})

