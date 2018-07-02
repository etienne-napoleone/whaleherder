FROM python:3-alpine

LABEL maintainer="etienne@tomochain.com"

WORKDIR /app

COPY ./whaleherder/ ./
COPY ./requirements.txt ./

RUN pip install -r requirements.txt

ENTRYPOINT ["gunicorn", "app:app", "-b", "0.0.0.0"]
