from celery import shared_task 
from django.core.management import call_command

@shared_task
def fetch_fpl_data():
    call_command("fetch_fpl_data")
