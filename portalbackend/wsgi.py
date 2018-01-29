"""
WSGI config for portalbackend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

'''with open('./Heroku.Env.Vars') as f:
    for line in f:
        # then, split name / value pair
        key, value = line.replace('export ', '', 1).strip().split('=', 1)
        os.environ[key] = value'''

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portalbackend.settings")

application = get_wsgi_application()
