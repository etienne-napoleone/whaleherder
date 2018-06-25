FROM python:3-alpine

LABEL maintainer="etienne@tomochain.com"

WORKDIR /app

COPY ./whaleherder/ ./
COPY ./Pipfile* ./

RUN pip install pipenv && \
    pipenv install --system

ENTRYPOINT ["gunicorn", "app:app", "-b", "0.0.0.0"]
