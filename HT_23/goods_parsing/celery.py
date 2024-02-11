import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'goods_parsing.settings')

app = Celery('goods_parsing')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
