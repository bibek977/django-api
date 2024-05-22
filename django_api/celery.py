import os
from celery import Celery
from dotenv import load_dotenv

load_dotenv()

if os.environ.get("DEBUG") == "TRUE":
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_api.settings.dev')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_api.settings.prod')

app = Celery()

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()