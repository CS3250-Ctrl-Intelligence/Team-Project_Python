from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist

from ci_shop.models import Product
from ci_cart.models import Cart,CartItem

def _cart_session(request):
    cart = request.session.session_key
    # if there is no session,create one
    if not cart:
        cart = request.session.create()
    return cart

def cart_add(request, product_id):
    product = Product.objects.get(id=product_id) # get product
    # if cart exist, get cart data using cart_id in the session
    try:
        cart = Cart.objects.get(cart_id=_cart_session(request)) 
    # if cart does not exist
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id= _cart_session(request)
        )
    cart.save()
    # if product already exist, retrieve the product data to increase quantity
    try:
        # check to see if user is logged in
        if request.user.is_authenticated:
            cart_items = CartItem.objects.get(user=request.user,product = product)
            cart_items.quantity +=1 # increase the quantity of that prduct 
            cart_items.save() # save updated quantity
        else:
            cart_items = CartItem.objects.get(product = product, cart = cart)
            cart_items.quantity +=1 # increase the quantity of that prduct 
            cart_items.save() # save updated quantity
    except CartItem.DoesNotExist:
        # if product don't exist, create a new product with initial quantity of 1
        if request.user.is_authenticated:
            cart_items =CartItem.objects.create(user = request.user,product =product, quantity =1, cart = cart)
        else:
            cart_items = CartItem.objects.create(product=product, quantity = 1, cart = cart)
        cart_items.save() # save new item
    
    # return HttpResponse(cart_item.product)
    return redirect('cart')


def cart(request, total=0, quantity = 0, cart_items = None,tax=0, grand_total = 0):
    try:
        if request.user.is_authenticated:
           cart_items = CartItem.objects.filter(user=request.user, is_active= True)
        else: 
            cart = Cart.objects.get(cart_id = _cart_session(request))
            cart_items = CartItem.objects.filter(cart = cart, is_active= True)
        # loop through the items in cart to find total and quantity
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity
        tax = (2* total)/100 #.2 tax
        grand_total = total+tax
    except ObjectDoesNotExist:
        pass #just ignore
    context ={
    'total':total,
    'quantity':quantity,
    'cart_items': cart_items,
    'tax':tax,
    'grand_total':grand_total,
    }
    return render(request,'cart.html',context)


def cart_remove(request,product_id):
    if request.user.is_authenticated:
        product = get_object_or_404(Product,id = product_id)
        cart_item = CartItem.objects.get(user=request.user,product = product)
    else:
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

    # This function uses the render() function to create the HttpResponse that is sent back to the browser. 
    # This function is a shortcut; it creates an HTML file by combining a specified HTML template and some 
    # data to insert in the template (provided in the variable named "context").
@login_required(login_url='login')
def checkout(request, total=0, quantity = 0, cart_items = None,tax=0, grand_total = 0):
    
    """ This function will query through the user's cart and populate"""
    try:
        #cart = Cart.objects.get(cart_id = _cart_session(request))
        cart_items = CartItem.objects.filter(user=request.user, is_active= True)
        # loop through the items in cart to find total and quantity
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity
        tax = (2* total)/100 #.2 tax
        grand_total = total+tax
    except Cart.DoesNotExist:
        pass #just ignore

    # A dict to be used as the template’s context for rendering the checkout page
    context ={
    'total':total,
    'quantity':quantity,
    'cart_items': cart_items,
    'tax':tax,
    'grand_total':grand_total,
    }
  
    return render(request,'checkout.html',context)
