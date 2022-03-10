from django.db import models

class Product(models.Model):
    product_id = models.CharField(max_length=100)
    quantity = models.IntegerField()
    wholesale_cost = models.DecimalField(max_digits=7, decimal_places=2)
    sale_price = models.DecimalField(max_digits=7, decimal_places=2)
    supplier_id = models.CharField(max_length=100)

    
    def __str__(self):
        return self.product_id