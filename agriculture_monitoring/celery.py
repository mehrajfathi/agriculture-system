import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'agriculture_monitoring.settings')

app = Celery('agriculture_monitoring')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# Define periodic tasks
app.conf.beat_schedule = {
    'check-irrigation-needs': {
        'task': 'core.tasks.check_irrigation_needs',
        'schedule': 3600.0,  # Run every hour
    },
    'check-weather-conditions': {
        'task': 'core.tasks.check_weather_conditions',
        'schedule': 1800.0,  # Run every 30 minutes
    },
} 