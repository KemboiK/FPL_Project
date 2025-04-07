from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fpl_project.settings")

app = Celery("fpl_project")

# Load task modules from all registered Django app configs.
app.config_from_object("django.conf:settings", namespace="CELERY")

# Autodiscover tasks in installed apps
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")

# Add the Periodic Task Schedule
app.conf.beat_schedule = {
    "fetch-fpl-data-every-5-mins": {
        "task": "fpl.tasks.fetch_fpl_data",  # Make sure this path is correct
        "schedule": crontab(minute="*/5"),  # Run every 5 minutes
    },
}
