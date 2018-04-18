release: python3 manage.py migrate;
web: gunicorn portalbackend.wsgi -t 45;coverage run --source=. manage.py test portalbackend -v 2 --liveserver=0.0.0.0:$PORT
worker: celery worker -A portalbackend --loglevel=debug --concurrency=4