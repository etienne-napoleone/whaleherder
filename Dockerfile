FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7

LABEL maintainer="etienne@tomochain.com"

WORKDIR /app

COPY ./app/ ./
COPY ./Pipfile* ./

RUN pip install pipenv && \
    pipenv sync
