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

    class Meta:
        db_table='payment_information'

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
    order_number = models.CharField(max_length=50)
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
    refund_requested = models.BooleanField(default=False)
    refund_granted= models.BooleanField(default=False)
    refund_allow = models.BooleanField(default=True)

    class Meta:
        db_table='orders'


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

    class Meta:
        db_table='order_items'
    def __str__(self):
        return self.product.product_id


class Refund(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    reason = models.TextField()
    accepted = models.BooleanField(default=False)

    class Meta:
        db_table='refund_information'
        
    def __str__(self):
        return str(self.pk)

class CustomerOrders(models.Model):
    date = models.DateField(blank=True, null=True)  # Field name made lowercase.
    cust_email = models.CharField(max_length=45, blank=True, null=True)
    cust_location = models.IntegerField(blank=True, null=True)    
    product = models.ForeignKey(Product, models.DO_NOTHING,to_field='product_id', blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'customer_orders'
        

