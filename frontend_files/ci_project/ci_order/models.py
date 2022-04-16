from django.db import models

from ci_account.models import Account
from ci_shop.models import Product


class Payment(models.Model):
    user = models. ForeignKey(Account,on_delete=models.CASCADE)
    payment_id = models.CharField(max_length=100)
    payment_method =models.CharField(max_length=100)
    amount_paid = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    created_at= models.DateTimeField(auto_now_add=True);

    def __str__(self):
        return self.payment_id

class Order(models.Model):
    STATUS=(
        ('New','New'),
        ('Accepted','Accepted'),
        ('Completed','Completed'),
        ('Cancelled','Cancelled'),

    )

    user = models.ForeignKey(Account, on_delete=models.SET_NULL, null = True)
    payment = models.ForeignKey(Payment, on_delete=models.SET_NULL, blank = True, null = True)
    order_number = models.CharField(max_length=20)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    address = models.CharField(max_length=50)
    zipcode  = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    tax = models.FloatField()
    status = models.CharField(max_length=10, choices=STATUS,default='New')
    is_ordered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    order_total = models.FloatField(default = 0)

    def __str__(self):
        return self.first_name

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment, on_delete=models.SET_NULL, blank = True, null = True)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.FloatField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.product.product_id