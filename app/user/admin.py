from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User, Wallet
from app.common.admin import BaseModelAdmin


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    ordering = ["-created"]


@admin.register(Wallet)
class OrderAdmin(BaseModelAdmin):
    list_display = (
        "user",
        "balance",
    )
    raw_id_fields = (
        "user",
    )
