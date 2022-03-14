from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404

from ci_shop.models import Product

from ci_cart.models import Cart,CartItem
# Create your views here.

def _cart_session(request):
    cart = request.session.session_key
    # if there is no session,create one
    if not cart:
        cart = request.session.create()
    return cart

def cart_add(request, product_id):
    product = Product.objects.get(id=product_id) # get product
    # if cart exist, get cart using cart_id in the session
    try:
        cart = Cart.objects.get(cart_id=_cart_session(request)) 
    # if cart does not exist
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id= _cart_session(request)
        )
    cart.save()

    try:
        cart_item = CartItem.objects.get(product = product, cart = cart)
        cart_item.quantity +=1 
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item =CartItem.objects.create(product =product, quantity =1, cart = cart)
        cart_item.save()
    
    # return HttpResponse(cart_item.product)
    return redirect('cart')


def cart(request, total=0, quantity = 0, cart_items = None):
    try:
        cart = Cart.objects.get(cart_id = _cart_session(request))
        cart_items = CartItem.objects.filter(cart = cart, is_active= True)
        # loop through the items in cart to find total and quantity
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity
        tax = (2* total)/100 #.2 tax
        grand_total = total+tax
    except Cart.DoesNotExist:
        pass #just ignore
    return render(request,'cart.html',{'total':total,'quantity':quantity,'cart_items': cart_items,'tax':tax,'grand_total':grand_total,})


def cart_remove(request,product_id):
    cart = Cart.objects.get(cart_id = _cart_session(request))
    product = get_object_or_404(Product,id = product_id)
    cart_item = CartItem.objects.get(product = product, cart = cart)
    # if there's item in cart, decrement by 1
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart')

def cart_item_remove(request,product_id):
    cart = Cart.objects.get(cart_id = _cart_session(request))
    product = get_object_or_404(Product,id = product_id)
    cart_item = CartItem.objects.get(product = product, cart = cart)

    cart_item.delete()
    return redirect('cart')



    