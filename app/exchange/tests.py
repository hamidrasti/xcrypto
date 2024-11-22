from django.contrib.auth import get_user_model

from app.common.tests import BaseTestCase
from .services import ExchangeService

User = get_user_model()


class ExchangeTestCase(BaseTestCase):
    def setUp(self):
        self.user = User.objects.create(username="testuser")
        self.wallet = self.user.wallet
        self.wallet.balance = 100.0
        self.wallet.save()

    def test_deduct_wallet_balance(self):
        ExchangeService.deduct_wallet_balance(self.user, 10.0)
        self.assertEqual(self.user.wallet.balance, 90.0)
