from .base import *

DEBUG = True
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "django",
        "USER": "django",
        "PASSWORD": "secret",
        "HOST": "django-postgres",
        "PORT": "5432",
    }
}

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
