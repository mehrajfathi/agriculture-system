#!/bin/bash

echo "Deploying Agriculture Monitoring System..."

# Activate virtual environment
source venv/bin/activate

# Install/upgrade dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput

# Run migrations
python manage.py migrate

# Restart services
sudo systemctl restart uwsgi
sudo systemctl restart nginx

# Restart Celery workers
sudo systemctl restart celery
sudo systemctl restart celerybeat

echo "Deployment completed successfully!" 