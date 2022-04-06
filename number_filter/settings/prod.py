import os

import django_heroku

from .settings import *

DEBUG = True
ALLOWED_HOSTS = [
    "http://spamnumberfilter.herokuapp.com",
    "http://spamnumberfilter.herokuapp.com/",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("NAME"),
        "USER": os.environ.get("USER"),
        "PASSWORD": os.environ.get("PASSWORD"),
        "HOST": os.environ.get("HOST"),
        "PORT": "5432",
    }
}

django_heroku.settings(locals())
