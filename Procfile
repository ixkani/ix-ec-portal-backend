release: python manage.py migrate;python manage.py test
web: gunicorn portalbackend.wsgi -t 45;
web:
worker: celery worker -A portalbackend --loglevel=debug --concurrency=4