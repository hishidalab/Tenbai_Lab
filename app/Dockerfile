FROM python:3.10.6-slim-buster
ENV PYTHONBURRERED=1
WORKDIR /django
RUN pip install --upgrade pip
RUN pip install django-allauth
RUN pip install Pillow
RUN apt-get update && \
    apt-get -y install gcc libmariadb-dev mariadb-client
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt