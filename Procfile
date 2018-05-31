release: bash ./release.sh
web: gunicorn portalbackend.wsgi -t 45
worker: celery worker -A portalbackend --loglevel=debug --concurrency=4