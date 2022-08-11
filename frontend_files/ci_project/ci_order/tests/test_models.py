from django.test import TestCase
from ci_order.models import Payment
from ci_account.models import Account

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