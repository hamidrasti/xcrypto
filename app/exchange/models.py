from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from app.common.models import BaseModel


class Crypto(BaseModel, models.Model):
    name = models.CharField(max_length=10)
    is_active = models.BooleanField(_("active"), default=True)

    def __str__(self):
        return f"{self.name}"


class Order(models.Model):
    crypto = models.ForeignKey(
        Crypto,
        on_delete=models.PROTECT,
        verbose_name=_("crypto"),
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name=_("user"),
    )
    amount = models.DecimalField(max_digits=24, decimal_places=8)
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    is_settled = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.id}"

    @property
    def total_price(self):
        return self.price_per_unit * self.amount
