from django.test import TestCase
from ci_shop.models import Product

# Testing shop.models Product class 
class ProductModelTest(TestCase):

    def setUp(self):
        self.data1 = Product.objects.create(
            product_id='123456',
            quantity='7',
            wholesale_cost='10.77',
            sale_price='17',
            supplier_id='ABC'
            )

    def test_productId(self):
        data = self.data1
        self.assertEqual(str(data), '123456')