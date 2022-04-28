from django.db import models
from django.urls import reverse

# Create your models here.

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.CharField(max_length=100,unique=True)
    quantity = models.IntegerField(null=True)
    wholesale_cost = models.DecimalField(max_digits=7, decimal_places=2)
    sale_price = models.DecimalField(max_digits=7, decimal_places=2)
    supplier_id = models.CharField(max_length=100, null = True)    
    slug = models.SlugField(max_length = 100,unique = True)
    in_stock = models.BooleanField(default = True)
    featured = models.BooleanField(default = False)
    
    class Meta:
        db_table='product'

    def get_url(self):
        return reverse('product_detail',args=[self.slug])

    def __str__(self):
        return self.product_id