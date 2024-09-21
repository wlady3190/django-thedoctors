FROM python:3.11.4-slim-bullseye

ENV PYTHONUNBUFFERED 1

ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update

RUN apt-get -y install python3-pip python3-cffi python3-brotli libpango-1.0-0 libpangoft2-1.0-0

RUN pip install --upgrade pip

WORKDIR /app

COPY ./requirements.txt /app/

RUN pip install --no-cache-dir -r /app/requirements.txt

COPY . /app/


ENTRYPOINT [ "sh", "/app/entrypoint.sh" ]

