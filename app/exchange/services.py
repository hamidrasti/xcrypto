from decimal import Decimal

from django.db import transaction
from django.db.models import F, DecimalField, Sum
from django.utils.translation import gettext as _

from app.api.exceptions import APIError
from .models import Order


class ExchangeService:
    CRYPTO_PRICES = {
        "ALPHA": Decimal(1.0),
        "BETA": Decimal(2.0),
        "GAMMA": Decimal(3.0),
        "DELTA": Decimal(5.0),
        "EPSILON": Decimal(8.0),
        "ZETA": Decimal(13.0),
    }
    MIN_PRICE_LIMIT = Decimal(10.0)

    @staticmethod
    def buy_from_exchange(crypto, amount):
        # Simulate an external API call to international exchanges
        print(f"Buy {amount} of {crypto} from exchange...")

    @staticmethod
    def deduct_wallet_balance(user, amount):
        wallet = user.wallet
        if wallet.balance < amount:
            raise APIError(
                cause=_("Insufficient wallet balance."),
                extra={
                    "error_code": 2001,
                    "error_detail": "Insufficient wallet balance.",
                    "error_scope": APIError.Scope.EXCHANGE,
                },
            )
        wallet.balance -= amount
        wallet.save()

    @classmethod
    def settle_orders(cls, crypto):
        unsettled_orders = Order.objects.filter(
            crypto=crypto,
            is_settled=False,
        )
        unsettled_stats = unsettled_orders.aggregate(
            amount_sum=Sum("amount"),
            total_price_sum=Sum(
                F("price_per_unit") * F("amount"),
                output_field=DecimalField(),
            ),
        )

        # orders_amount = sum(order.amount for order in unsettled_orders)
        # orders_total_price = sum(order.total_price for order in unsettled_orders)
        orders_amount = unsettled_stats["amount_sum"]
        orders_total_price = unsettled_stats["total_price_sum"]

        if orders_total_price >= cls.MIN_PRICE_LIMIT:
            cls.buy_from_exchange(crypto, orders_amount)
            unsettled_orders.update(is_settled=True)

    @classmethod
    @transaction.atomic
    def create_order(cls, user, crypto, amount):

        if crypto.name not in cls.CRYPTO_PRICES:
            raise APIError(
                cause=_("Unavailable crypto."),
                extra={
                    "error_code": 2002,
                    "error_detail": "Unavailable crypto.",
                    "error_scope": APIError.Scope.EXCHANGE,
                },
            )

        price_per_unit = cls.CRYPTO_PRICES.get(crypto.name)
        total_price = price_per_unit * amount

        cls.deduct_wallet_balance(user, total_price)

        order = Order.objects.create(
            user=user,
            crypto=crypto,
            amount=amount,
            price_per_unit=price_per_unit,
        )

        cls.settle_orders(crypto)

        return order
