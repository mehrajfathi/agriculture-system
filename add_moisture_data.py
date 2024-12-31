import os
import django
import sys

# Set up Django environment
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'agriculture_monitoring.settings')
django.setup()

from farm_management.models import FarmPlot, MoistureReading
from django.utils import timezone
from datetime import timedelta
import random

def add_moisture_readings():
    try:
        # Get your plot
        plot = FarmPlot.objects.get(id=4)  # Using plot ID 4
        
        # Create 7 days of sample readings
        for i in range(7):
            timestamp = timezone.now() - timedelta(days=i)
            moisture = random.uniform(30, 60)  # Random value between 30-60%
            MoistureReading.objects.create(
                plot=plot,
                moisture_level=moisture,
                timestamp=timestamp
            )
        print("Created sample moisture readings")
        
    except FarmPlot.DoesNotExist:
        print("Plot with ID 4 not found")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    add_moisture_readings() 