# Testing account.models Account class 
from django.test import TestCase
from ci_account.models import Account
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