FROM python:3.11.4-slim-bullseye
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
RUN apt-get update
RUN apt-get -y install python3-pip python3-cffi python3-brotli libpango-1.0-0 libpangoft2-1.0-0

RUN pip install --upgrade pip

COPY ./requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ./homepage /app/homepage
COPY ./core /app/core
COPY ./appointment /app/appointment
COPY ./appointment_schedule /app/appointment_schedule
COPY ./doctors /app/doctors
COPY ./patients /app/patients
COPY ./patients_images /app/patients_images
COPY ./manage.py /app/manage.py
COPY ./entrypoint.sh /app/entrypoint.sh 
RUN chmod +x /app/entrypoint.sh


WORKDIR /app

RUN mkdir -p /app/staticfiles

ENTRYPOINT [ "sh", "/app/entrypoint.sh" ]



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