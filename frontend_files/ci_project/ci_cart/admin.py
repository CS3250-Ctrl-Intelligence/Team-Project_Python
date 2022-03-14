from django.contrib import admin

from ci_cart.models import Cart,CartItem
# Register your models here.


admin.site.register(Cart)
admin.site.register(CartItem)