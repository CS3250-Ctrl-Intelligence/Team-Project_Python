from django.test import TestCase,override_settings
from django.test import Client
from django.urls import reverse
from django.http import HttpRequest
from django.conf import settings
from django.template.loader import render_to_string

from importlib import import_module
from ci_shop.models import Product
from ci_account.models import Account
from ci_shop.views import shop,product_detail

@override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
class TestViewResponses(TestCase):
    def setUp(self):
        self.client =Client()
        Account.objects.create_user(first_name = 'Brian', 
            last_name = 'V',
            username = 'B7',
            email="B@LIVE.COM",
            password= '123456',
           )
        Product.objects.create(product_id='Test',quantity='4',wholesale_cost ='10.24',sale_price='1.52',supplier_id='Walmart',slug='test')

    def test_shoppage_url(self):
        """Test shoppage response status"""
        response = self.client.get('/shop/')
        self.assertEqual(response.status_code,200)
    
    def test_product_detail_url(self):
        """Test product detail response status"""
        response = self.client.get(reverse('product_detail',args=['test']))
        self.assertEqual(response.status_code,200)

