from celery import shared_task

from .models import Crypto
from .services import ExchangeService


@shared_task
def settle_small_orders_task():
    """
    Task to process and settle small orders (less than $10) periodically.
    """

    for crypto in Crypto.objects.filter(is_active=True).iterator():
        ExchangeService.settle_orders(crypto)
