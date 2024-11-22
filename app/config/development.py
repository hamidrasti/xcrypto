from .base import *  # NOQA

DEBUG = True

ALLOWED_HOSTS = [
    "0.0.0.0",
    "127.0.0.1",
    "localhost",
    "localhost:8000",
] + env.list("ALLOWED_HOSTS", default=[])

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
] + env.list("CORS_ALLOWED_ORIGINS", default=[])

CORS_ALLOWED_ORIGIN_REGEXES = [
    r"^http:\/\/localhost.*",
]

CELERY_BROKER_BACKEND = "memory"
# CELERY_TASK_ALWAYS_EAGER = True
# CELERY_TASK_EAGER_PROPAGATES = True
