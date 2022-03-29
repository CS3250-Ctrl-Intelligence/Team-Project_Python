from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100,unique= True)
    cat_photo = models.ImageField(upload_to='static/images', null = True)
    
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('prods_by_cat',args=[self.slug])
        
    def __str__(self):
        return self.name