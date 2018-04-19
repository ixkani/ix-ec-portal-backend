release: python manage.py migrate;coverage report
web: gunicorn portalbackend.wsgi -t 45;
web: coverage report
worker: celery worker -A portalbackend --loglevel=debug --concurrency=4