release: python manage.py migrate;python manage.py test --liveserver=0.0.0.0:$PORT;
web: gunicorn portalbackend.wsgi -t 45;
worker: celery worker -A portalbackend --loglevel=debug --concurrency=4