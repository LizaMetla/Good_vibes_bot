import os

from celery import Celery
from celery.schedules import crontab

from django.apps import apps

__all__ = ["app"]

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "goodVibes.settings")

app = Celery("goodVibes")
app.config_from_object("django.conf:settings")
app.autodiscover_tasks(lambda: [cfg.name for cfg in apps.get_app_configs()])
