from django.db import models

from ci_account.models import Account
from ci_shop.models import Product
# Create your models here.


class Cart(models.Model):
    cart_id = models.CharField(max_length=200, blank = True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table='carts'

    def __str__(self):
        return self.cart_id

    
class CartItem(models.Model):
    
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null = True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE, null = True)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table='cart_items'

    def sub_total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return str(self.product)