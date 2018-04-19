release: python manage.py migrate
web: coverage run --source=. --omit=*/migrations/*,*/v0/*  manage.py test portalbackend -v 2;coverage html
worker: celery worker -A portalbackend --loglevel=debug --concurrency=4