from django.db import models
from ci_app.models.product import Product
from ci_app.models.customer_order import CustomerOrder

class CustomerOrderItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,blank = True, null = True)
    order = models.ForeignKey(CustomerOrder, on_delete= models.SET_NULL, blank = True, null = True)

    date_ordered = models.DateField(auto_now_add= True)
    cust_email= models.EmailField(max_length=100, null= True)
    cust_location = models.IntegerField(default=0,null = True, blank = True)
    quantity = models.IntegerField(default = 0, null = True, blank = True)

    @property
    def get_total(self):
        total = self.product.sale_price * self.quantity
        return total

    def __str__(self):
        return self.cust_email +","+str(self.cust_location) 
