release: python3 manage.py migrate;coverage html
web: gunicorn portalbackend.wsgi -t 45
worker: celery worker -A portalbackend --loglevel=debug --concurrency=4