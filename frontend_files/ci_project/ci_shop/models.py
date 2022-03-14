from django.db import models
from django.urls import reverse
from ci_category.models import Category
# Create your models here.

class Product(models.Model):
    product_id = models.CharField(max_length=100)
    quantity = models.IntegerField()
    wholesale_cost = models.DecimalField(max_digits=7, decimal_places=2)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    slug = models.SlugField(max_length = 200,unique = True)
    in_stock = models.BooleanField(default = True)
    # CASCADE = when the category is deleted, the products tied to that category is also deleted
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def get_url(self):
        return reverse('product_detail',args=[self.category.slug, self.slug])

    def __str__(self):
        return self.product_id