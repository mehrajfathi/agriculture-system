import os
import django
import sys

# Set up Django
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'agriculture_monitoring.settings')
django.setup()

from farm_management.models import Crop

def load_crops():
    crops = [
        {
            'name': 'rice',
            'description': 'Rice is a staple food crop.',
            'soil_type': 'Clay or clay loam',
            'climate_requirements': 'Hot and humid climate',
            'growing_season': '90-150 days',
            'water_requirements': '1000-2000mm water',
            'fertilizer_requirements': 'NPK ratio 120:60:60'
        },
        # Add other crops here
    ]

    for crop_data in crops:
        Crop.objects.get_or_create(**crop_data)
        print(f"Added crop: {crop_data['name']}")

if __name__ == '__main__':
    load_crops() 