import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.config.development")

celery_app = Celery("xcrypto")
celery_app.config_from_object("django.conf:config", namespace="CELERY")
celery_app.autodiscover_tasks()
