from django.db import models

from frontend_files.ci_project.ci_app.models.inventory import Inventory

class CustomerOrder(models.Model):
    date = models.DateField()
    cust_email= models.EmailField(max_length=100)
    cust_location = models.IntegerField()
    product_id = models.ForeignKey(Inventory)
    quantity = models.IntegerField()

    
    def __str__(self):
        return self.cust_email +","+self.cust_location