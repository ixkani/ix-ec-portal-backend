release: coverage run --source=. manage.py test portalbackend -v 2
web: gunicorn portalbackend.wsgi -t 45;
worker: celery worker -A portalbackend --loglevel=debug --concurrency=4