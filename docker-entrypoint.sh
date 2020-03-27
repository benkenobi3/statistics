#!/bin/sh

python3 manage.py check && \
    python3 manage.py collectstatic --no-input && \
    python3 manage.py migrate --no-input && \
    gunicorn --config gunicorn.conf.py app.wsgi:application