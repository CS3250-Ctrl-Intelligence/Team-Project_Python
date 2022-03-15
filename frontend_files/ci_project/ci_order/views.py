from django.shortcuts import render,redirect

from ci_cart.models import CartItem,Cart
from ci_order.forms import OrderForm
from ci_order.models import Order,OrderItem

def place_order(request,total =0, quantity = 0):
    current_user = request.user
    grand_total = 0
    tax = 0
    # Check to see if cart count is less than or equal to 0, if so redirect to shop

    cart_items = CartItem.objects.filter(user=current_user)
    cart_count = cart_items.count()
    if (cart_count <= 0):
        return redirect('shop')

    for cart_item in cart_items:
        total += (cart_item.product.price * cart_item.quantity)
        quantity += cart_item.quantity

    tax = (2* total)/100 #.2 tax
    grand_total = total+tax
    
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            # store all the billing info inside order table
            data = Order()
            data.first_name = form.cleaned_data('first_name')
            data.last_name = form.cleaned_data('last_name')
            data.email = form.cleaned_data('email')
            data.address = form.cleaned_data('address')
            data.country = form.cleaned_data('country')
            data.state = form.cleaned_data('state')
            data.city = form.cleaned_data('city')
            data.tax = tax
            data.order_total = grand_total
            data.save()
            