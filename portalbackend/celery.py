from __future__ import absolute_import
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portalbackend.settings')

from django.conf import settings
from celery import Celery

# Create celery instance, named portalbackend
app = Celery('portalbackend')

# get broker + backend settings from main settings file
app.config_from_object('django.conf:settings')

# discover tasks in all applications, must be in installed Apps
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

