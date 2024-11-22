from django.contrib import admin

from app.common.admin import BaseModelAdmin
from .models import Crypto, Order


@admin.register(Crypto)
class CryptoAdmin(BaseModelAdmin):
    list_display = ("name", "is_active")


@admin.register(Order)
class OrderAdmin(BaseModelAdmin):
    list_display = (
        "crypto",
        "user",
        "total_price",
        "amount",
        "price_per_unit",
        "is_settled",
    )
    raw_id_fields = (
        "crypto",
        "user",
    )
