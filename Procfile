release: python manage.py migrate
web: gunicorn portalbackend.wsgi -t 45;gunicorn coverage run --source=. --omit=*/migrations/*,*/v0/*  manage.py test portalbackend -v 2;gunicorn coverage html
worker: celery worker -A portalbackend --loglevel=debug --concurrency=4