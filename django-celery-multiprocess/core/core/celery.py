from __future__ import absolute_import,unicode_literals
import os
from celery import Celery
from django.conf import settings

"""
celery -A core.celery worker --pool=solo -l info [for celery worker]
celery -A core beat -l info [for celery beat ]

"""
# celery main config

os.environ.setdefault('DJANGO_SETTINGS_MODULE','core.settings')

app=Celery('core')
app.conf.enable_utc=False
app.conf.update(timezone='Asia/Kolkata')

app.config_from_object(settings,namespace='CELERY')

# celery beat conf..[scheduler]
from celery.schedules import crontab

app.conf.beat_schedule={
    'send_mail_everyday_at_12pm':{ #static task define
        'task': 'celery1.task.schedule_mail_to_all',
        'schedule':crontab(hour=12,minute=51),
        #'args':(2,) [arguements for that func]
    }
}
app.autodiscover_tasks()

@app.task(bind=True)
def debug_tsak(self):
    print(f'request : {self.request!r}')