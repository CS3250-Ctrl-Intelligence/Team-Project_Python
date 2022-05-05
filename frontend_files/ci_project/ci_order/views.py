import datetime
import json
from datetime import date

today = date.today()
from django.http import JsonResponse
from django.shortcuts import render,redirect
from django.views import View
from django.conf import settings
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import EmailMessage,EmailMultiAlternatives,send_mail
from django.template.loader import render_to_string
from django.template import loader


from ci_cart.models import CartItem,Cart
from ci_order.forms import OrderForm,RefundForm
from ci_order.models import Order,OrderItem,Payment,Refund,CustomerOrders
from ci_shop.models import Product




def payments(request):
    body = json.loads(request.body)

    order = Order.objects.get(user=request.user,is_ordered = False, order_number =body['orderID'])

    
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
        orderitem.price = items.product.sale_price
        orderitem.ordered = True
        orderitem.save()

        # Create new order for customer_order table
        customer_order = CustomerOrders()
        customer_order.date = today.strftime("%Y-%m-%d")
        customer_order.cust_email=order.email
        customer_order.cust_location= order.zipcode
        customer_order.quantity= items.quantity
        product = Product.objects.get(pk=items.product_id)
        customer_order.product_id = product.product_id
        customer_order.save()

        # Reduce the quantity of sold products in inventory
        # product = Product.objects.get(id=items.product_id)
        # product.quantity -= items.quantity
        # product.save()

    # filter most expensive item in order
    # most_expensive = OrderItem.objects.filter(user=request.user).order_by('-price')[:1].get()
    # print(most_expensive.product.supplier_id)
    # products_based_on_supplier = Product.objects.filter(supplier_id= most_expensive.product.supplier_id)[:4]
    # for i in products_based_on_supplier:
    #     print(i)

    # filter highest quantity in ordered history
    highest_quantity= OrderItem.objects.filter(user=request.user).order_by('-quantity')[:1].get()
    print(highest_quantity)
    products_based_on_supplier = Product.objects.filter(supplier_id=highest_quantity.product.supplier_id).exclude(slug=highest_quantity.product.slug)[:6]
  

    
    
    
    # Clear cart
    CartItem.objects.filter(user=request.user).delete()

    order_detail = OrderItem.objects.filter(order__order_number=body['orderID'])
    subtotal=0
    for i in order_detail:
        subtotal+= i.price * i.quantity
    subtotal = round(subtotal,2)
    
    # Send email to customer
    
    context={'user':request.user,'order':order,'order_detail':order_detail,'subtotal':subtotal,'recommendation':products_based_on_supplier}

    html_template = 'order_confirmation.html'
    html_message = render_to_string(html_template, context)
    subject = 'Thank You For Your Order!'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [request.user.email]
    message = EmailMessage(subject, html_message,
                            email_from, recipient_list)
    message.content_subtype = 'html'
    message.send()
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
        total += (cart_item.product.sale_price * cart_item.quantity)
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
    

class RequestRefundView(View):
    def get(self,*args,**kwargs):
        form = RefundForm()
        context={
            'form':form
        }
        return render(self.request,"refund.html",context)

    def post(self,*args, **kwargs):
        form = RefundForm(self.request.POST)
        if form.is_valid():
            order_num = form.cleaned_data.get('order_num')
            message = form.cleaned_data.get('message')
            # edit the order
            try:
                order = Order.objects.get(order_number = order_num)
                order.refund_requested = True
                order.save()

            # store refund
                refund = Refund()
                refund.order = order
                refund.reason = message
                refund.save()
                messages.success(self.request,messages.INFO,f"Your request was received")
                return redirect("request-refund")
            except ObjectDoesNotExist:
                messages.info(self.request,f"This order does not exist")
                return redirect("request-refund") # return to the same page

                