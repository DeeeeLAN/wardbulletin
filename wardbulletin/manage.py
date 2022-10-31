#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import environ


def main():
    """Run administrative tasks."""
    env = environ.Env()
    env_file = (environ.Path(__file__) - 1)('.env')
    env.read_env(env_file)
    # os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'wardbulletin.settings.{env.str("DJANGO_SETTINGS_MODULE")}')
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'wardbulletin.settings.dev')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
