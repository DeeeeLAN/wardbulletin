'''Use this for production'''

from .base import *

URL = 'https://wardbulletin.com/'  # TODO: replace with correct URL
DEBUG = False

ALLOWED_HOSTS += ['.wardbulletin.com']  # TODO: replace with correct URL
WSGI_APPLICATION = 'wardbulletin.wsgi.prod.application'

CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = (
    'https://wardbulletin.com',  # TODO: replace with correct URL
)

CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 60 * 60
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
