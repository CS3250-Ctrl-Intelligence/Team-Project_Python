from django.contrib import admin
from ci_shop.models import Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_diplay =('product_id','wholesale_cost','sale_price', 'quantity')
    prepopulated_fields = {'slug':('product_id',)}
admin.site.register(Product, ProductAdmin)