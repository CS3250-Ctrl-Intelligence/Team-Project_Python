from django.db import models
from ci_app.models.product import Product
from ci_app.models.customer import Customer

class CustomerOrder(models.Model):
    customer = models.ForeignKey(Customer, on_delete= models.SET_NULL, blank = True, null = True)
    date_ordered =models.DateField(auto_now_add= True)

    def __str__(self):
        return str(self.id)
