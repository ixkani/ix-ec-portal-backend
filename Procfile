release: python3 manage.py migrate;coverage erase;coverage run --source=. --omit=*/migrations/*,*/v0/*  manage.py test portalbackend -v 2;coverage report;coverage html -d /tmp;
web: gunicorn portalbackend.wsgi -t 45
worker: celery worker -A portalbackend --loglevel=debug --concurrency=4