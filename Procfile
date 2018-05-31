release: python3 manage.py migrate;coverage run --source=. --omit=*/migrations/*,*/v0/*,*/python/*  manage.py test portalbackend -v 2;coverage report;bandit -r portalbackend
web: gunicorn portalbackend.wsgi -t 45
worker: celery worker -A portalbackend --loglevel=debug --concurrency=4