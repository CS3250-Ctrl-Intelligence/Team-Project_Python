from django.contrib import admin
from ci_order.models import Order,OrderItem,Payment
# Register your models here.

# Diplay OrderItem table in line with Order table
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra =0
    readonly_fields=['payment','user','product','quantity','price','ordered']

class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display =['order_number','first_name','last_name','email', 'address','order_total','tax', 'status','is_ordered', 'created_at']
    list_filter =['status','is_ordered']
    search_fields = ['order_number','first_name','last_name','email']
    list_per_page = 20

    inlines=[OrderItemInline]

admin.site.register(Order,OrderAdmin)
admin.site.register(OrderItem)
admin.site.register(Payment)