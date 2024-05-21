FROM python:3

ENV PYTHONUNBUFFERED=1

WORKDIR /django_api

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . /django_api