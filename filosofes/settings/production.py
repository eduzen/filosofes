import os

from .base import *  # NOQA


SECRET_KEY = os.environ.get("SECRET_KEY")

SITE_ID = 1

ALLOWED_HOSTS = [
    "www.filosofes.com.ar",
    "filosofes.com.ar",
    "books.filosofes.com.ar",
    "blog.filosofes.com.ar",
    "authors.filosofes.com.ar",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("DB_NAME"),
        "USER": os.environ.get("DB_USER"),
        "PASSWORD": os.environ.get("DB_PASS"),
        "HOST": os.environ.get("DB_SERVICE"),
        "PORT": os.environ.get("DB_PORT"),
    }
}
