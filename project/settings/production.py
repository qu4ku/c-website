from .base import *
import os


# Override base.py settings here
DEBUG = False
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('NAME')
        'USER': os.environ.get('USER')
        'PASSWORD': os.environ.get('PASSWORD')
        'HOST': 'localhost',
        'PORT': '',
    }
}

