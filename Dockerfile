FROM python:3

ENV PYTHONUNBUFFERED=1

RUN apt-get update && \
    apt-get install -y \
    libpq-dev \
    gcc \
    python3-dev \
    musl-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /django_api

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . /django_api