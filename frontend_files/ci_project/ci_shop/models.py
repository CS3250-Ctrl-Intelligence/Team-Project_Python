from django.db import models
from django.urls import reverse

# Create your models here.

class Product(models.Model):
    product_id = models.CharField(max_length=100)
    quantity = models.IntegerField()
    wholesale_cost = models.DecimalField(max_digits=7, decimal_places=2)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    supplier_id = models.CharField(max_length=100, null = True)    
    slug = models.SlugField(max_length = 200,unique = True)
    in_stock = models.BooleanField(default = True)
    featured = models.BooleanField(default = False)
    
    

    def get_url(self):
        return reverse('product_detail',args=[self.slug])

    def __str__(self):
        return self.product_id