import datetime
from django.http import JsonResponse
from django.shortcuts import render,redirect

from ci_cart.models import CartItem,Cart
from ci_order.forms import OrderForm
from ci_order.models import Order,OrderItem,Payment
from ci_shop.models import Product

import json

# Email
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

def payments(request):
    body = json.loads(request.body)

    order = Order.objects.get(user=request.user,is_ordered = False, order_number =body['orderID'])

    # print(body)
    # Store transaction details inside Payment model
    payment =Payment(
        user = request.user,
        payment_id = body['transID'],
        payment_method = body['payment_method'],
        amount_paid = order.order_total,
        status = body['status'],
    )
    payment.save()

    # Create order with payment and set is_ordered to True
    order.payment = payment
    order.is_ordered = True
    order.save()

    # Move the Cart Items to Order Item table
    cart_items = CartItem.objects.filter(user=request.user)
    for items in cart_items:
        orderitem = OrderItem()
        orderitem.order_id = order.id
        orderitem.payment = payment
        orderitem.user_id = request.user.id
        orderitem.product_id = items.product_id
        orderitem.quantity = items.quantity
        orderitem.price = items.product.price
        orderitem.ordered = True
        orderitem.save()

    # Reduce the quantity of sold products in inventory
        product = Product.objects.get(id=items.product_id)
        product.quantity -= items.quantity
        product.save()
    
    # Clear cart
    CartItem.objects.filter(user=request.user).delete()

    # Send email to customer
    mail_subject = 'Thank you for your order!'
    message = render_to_string('orderReceived.html',{
                    'user' :request.user,
                    'order':order,

            })
    to_email = request.user.email
    send_email = EmailMessage(mail_subject, message, to=[to_email])
    send_email.send()

    # Send order number and payment transaction id back to sendData function via JsonResponse and populate Thank you page
    data={
        'order_number':order.order_number,
        'transID':payment.payment_id,
    }
    return JsonResponse(data)
    #return render(request,'payment.html')

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
    tax=round(tax,2)
    grand_total = total+round(tax,2)
    
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            # store all the billing info inside order table
            data = Order()
            data.user = current_user
            data.first_name = form.cleaned_data['first_name']
            data.last_name = form.cleaned_data['last_name']
            data.email = form.cleaned_data['email']
            data.address = form.cleaned_data['address']
            data.zipcode = form.cleaned_data['zipcode']
            data.state = form.cleaned_data['state']
            data.city = form.cleaned_data['city']
            data.tax = tax
            data.order_total = grand_total
            data.save()

            # Generate order number
            year = int(datetime.date.today().strftime('%Y'))
            date = int(datetime.date.today().strftime('%d'))
            month = int(datetime.date.today().strftime('%m'))
            day = datetime.date(year,month,date)
            current_date = day.strftime("%Y%m%d")

            order_number = current_date + str(data.id)

            data.order_number = order_number
            data.save()


            order = Order.objects.get(user=current_user, is_ordered = False,order_number = order_number)
            context ={
                'order':order,
                'cart_items': cart_items,
                'tax':tax,
                'total':total,
                'grand_total': grand_total,
            }
            return render(request,'payment.html',context)
    else:
        return redirect('checkout')


def order_complete(request):
    order_number = request.GET.get('order_number')
    transId = request.GET.get('payment_id')

    try:
        order = Order.objects.get(order_number=order_number, is_ordered= True)
        ordered_items = OrderItem.objects.filter(order_id=order.id)
        payment = Payment.objects.get(payment_id=transId)

        subtotal = 0
        # Get subtotal
        for item in ordered_items:
            subtotal += item.price * item.quantity

        subtotal = round(subtotal,2)

        context = {
            'order':order,
            'ordered_items':ordered_items,
            'order_number':order.order_number,
            'transId': payment.payment_id,
            'payment': payment,
            'subtotal':subtotal,
        }
        return render(request,'order_complete.html',context)
    except(Payment.DoesNotExist,Order.DoesNotExist):
        return redirect('home')
    