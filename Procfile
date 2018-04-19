release: python manage.py migrate;coverage run --source=. --omit=*/migrations/*,*/v0/*  manage.py test portalbackend -v 2 --liveserver=0.0.0.0:$PORT;coverage html
web: gunicorn portalbackend.wsgi -t 45;
worker: celery worker -A portalbackend --loglevel=debug --concurrency=4