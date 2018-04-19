release: python manage.py migrate;
web: gunicorn portalbackend.wsgi -t 45;
web: gunicorn coverage report
worker: celery worker -A portalbackend --loglevel=debug --concurrency=4