FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7

LABEL maintainer="etienne@tomochain.com"

WORKDIR /app

COPY ./app/ ./
COPY ./Pipefile* ./

RUN pip install pipenv && \
    pipenv sync
