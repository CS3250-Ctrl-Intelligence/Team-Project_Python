from django.test import TestCase
from ci_cart.models import Cart

# Testing cart.models Cart class 
class CartModelTest(TestCase):

    def setUp(self):
        self.data1 = Cart.objects.create(
            cart_id='abcd',
            )

    def test_cartId(self):
        data = self.data1
        self.assertEqual(str(data), 'abcd')

