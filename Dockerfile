FROM python:alpine3.6

WORKDIR /app

COPY ./requirements.txt /app

RUN apk update && \
    apk add --no-cache --virtual build-deps gcc python3-dev musl-dev jpeg-dev zlib-dev libffi-dev && \
    apk add --no-cache postgresql-dev poppler-utils &&  pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    apk del build-deps

ENV DJANGO_ENV="DEBUG" \
    DJANGO_SECRET_KEY="ea0cd97ad90d22fe1c9624568d45b5f85987d8f80d9c6adb" \
    PORT="5000"

COPY ./ /app

VOLUME ["app/components"]

ENTRYPOINT ["/bin/sh", "docker-entrypoint.sh"]