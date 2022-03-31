from django.contrib import admin
from ci_shop.models import Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'wholesale_cost', 'price', 'quantity', 'supplier_id', 'featured',)
    list_editable = ('featured',)
    prepopulated_fields = {'slug':('product_id',)}
admin.site.register(Product, ProductAdmin)