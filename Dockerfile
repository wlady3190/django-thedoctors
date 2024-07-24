FROM python:3.11.4-slim-bullseye

RUN pip install --upgrade pip

COPY ./requirements.txt .

COPY ./core /app

WORKDIR /app

COPY ./entrypoint.sh /
ENTRYPOINT [ "sh", "/entrypoint.sh" ]



# ENV PYTHONUNBUFFERED 1
# ENV PYTHONDONTWRITEBYTECODE 1

# # install system dependencies
# RUN apt-get update

# # install dependencies
# RUN pip install --upgrade pip
# COPY ./requirements.txt /app/
# RUN pip install -r requirements.txt

# COPY . /app

# ENTRYPOINT [ "gunicorn", "core.wsgi", "-b", "0.0.0.0:8000"]