from django.test import TestCase
from ci_shop.models import Product
from ci_cart.models import Cart
from ci_order.models import Payment
from ci_account.models import Account

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

# Testing order.models Payment class 
class PaymentModelTest(TestCase):

    def setUp(self):
        self.user = Account.objects.create_user(
            first_name = 'Brian', 
            last_name = 'V',
            username = 'B7',
            email="B@LIVE.COM",
            password= '123456')
        self.data1 = Payment.objects.create(
            payment_id='abcd',
            payment_method='paypal',
            amount_paid='10.77',
            user= self.user,
            )

    def test_paymentId(self):
        data = self.data1
        self.assertEqual(str(data), 'abcd')

# Testing cart.models Cart class 
class CartModelTest(TestCase):

    def setUp(self):
        self.data1 = Cart.objects.create(
            cart_id='abcd',
            )

    def test_cartId(self):
        data = self.data1
        self.assertEqual(str(data), 'abcd')

# Testing account.models Account class 
class AccountModelTest(TestCase):

    def setUp(self):
        self.data1 = Account.objects.create_user(
            first_name = 'Brian', 
            last_name = 'V',
            username = 'B7',
            email="B@LIVE.COM",
            password= '123456',)

    def test_username(self):
        data = self.data1
        self.assertEqual(str(data), 'B7')