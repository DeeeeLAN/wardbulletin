"""
WSGI config for wardbulletin project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
import environ

from django.core.wsgi import get_wsgi_application

env = environ.Env()
env_file = (environ.Path(__file__) - 4)('.env')
env.read_env(env_file)
if env.str('DJANGO_SETTINGS_MODULE') in ['dev', 'prod']:
    os.environ['DJANGO_SETTINGS_MODULE'] = f'wardbulletin.settings.{env.str("DJANGO_SETTINGS_MODULE")}'
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wardbulletin.settings.prod')


application = get_wsgi_application()
