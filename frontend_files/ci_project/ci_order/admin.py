from django.contrib import admin
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings

from ci_order.models import Order,OrderItem,Payment,Refund,CustomerOrders
from ci_shop.models import Product


# refund admin action
def make_refund_acccepted(modeladmin,request,queryset):
    for i in queryset:
        if i.refund_granted:
            print("Already refunded")
        
        else:
            i.refund_requested = False

            i.refund_granted= True
            i.save()    
            


            # loop through items in order to add product quantity back to inventory
            order= Order.objects.get(order_number=i.order_number)
            order_items= OrderItem.objects.filter(order=order)
            for items in order_items:
                qtt = items.quantity
                product = Product.objects.get(product_id=items.product.product_id)
                product.quantity +=items.quantity
                product.save()

            # Send refund confirmation email to customer
            # mail_subject = 'Your order has been refunded'
            # message = render_to_string('refundGranted.html',{
            #         'first_name':i.first_name,
            #         'order_number':i.order_number,  
            #         'last_name':i.last_name,  
            #         })
            # to_email = i.email

            # send_email = EmailMessage(mail_subject, message, to=[to_email])
            # send_email.send()

            context={'user':request.user,'order':order}

            html_template = 'refundGranted.html'
            html_message = render_to_string(html_template, context)
            subject = 'Refund Confirmation'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [i.email]
            message = EmailMessage(subject, html_message,
                                    email_from, recipient_list)
            message.content_subtype = 'html'
            message.send()

make_refund_acccepted.short_description='Approve refund'




# Diplay OrderItem table in line with Order table
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra =0
    readonly_fields=['payment','user','product','quantity','price','ordered']

class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display =['order_number','first_name','last_name','email', 'address','order_total','tax', 'status','is_ordered','refund_requested','refund_granted', 'created_at']
    list_filter =['status','is_ordered']
    search_fields = ['order_number','first_name','last_name','email']
    list_per_page = 20

    inlines=[OrderItemInline]

    actions=[make_refund_acccepted]

admin.site.register(Order,OrderAdmin)
admin.site.register(OrderItem)
admin.site.register(Payment)
admin.site.register(Refund)
admin.site.register(CustomerOrders)