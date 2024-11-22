# Generated by Django 5.1.3 on 2024-11-22 11:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Crypto",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=10)),
                ("is_active", models.BooleanField(default=True, verbose_name="active")),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("amount", models.DecimalField(decimal_places=8, max_digits=24)),
                (
                    "price_per_unit",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                ("is_settled", models.BooleanField(default=False)),
                (
                    "crypto",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="exchange.crypto",
                        verbose_name="crypto",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="user",
                    ),
                ),
            ],
        ),
    ]
