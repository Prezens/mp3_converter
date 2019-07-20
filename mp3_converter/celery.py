import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mp3_converter.settings')

app = Celery('mp3_converter')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks()
