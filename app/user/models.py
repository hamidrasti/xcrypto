from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken

from app.common.mixins import TimestampMixin
from app.common.models import BaseModel


class User(AbstractUser, TimestampMixin):

    def generate_tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            "access_token": str(refresh.access_token),
            "refresh_token": str(refresh),
        }


class Wallet(TimestampMixin, BaseModel):
    balance = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0.00,
    )
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="wallet",
    )

    def __str__(self):
        return f"Wallet of {self.user.username}"
