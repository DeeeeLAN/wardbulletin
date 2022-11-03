'''Use this for production'''

from .base import *

URL = f'https://{env.str("DOMAIN")}/'
DEBUG = False

ALLOWED_HOSTS += [f'.{env.str("DOMAIN")}']
WSGI_APPLICATION = 'wardbulletin.wsgi.prod.application'

CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = (
    f'https://{env.str("DOMAIN")}',
)

# CSRF_COOKIE_SECURE = True
# SECURE_HSTS_SECONDS = 60 * 60
# SECURE_HSTS_PRELOAD = True
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# SECURE_SSL_REDIRECT = True
# SESSION_COOKIE_SECURE = True

