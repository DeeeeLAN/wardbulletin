'''Use this for development'''

from .base import *

URL = 'http://127.0.0.1:8000/'
ALLOWED_HOSTS += ['*']
DEBUG = True

WSGI_APPLICATION = 'wardbulletin.wsgi.dev.application'

CORS_ALLOW_ALL_ORIGINS = True
CORS_ORIGIN_WHITELIST = (
    'http://127.0.0.1:8000',
    'http://localhost:8000',
)
