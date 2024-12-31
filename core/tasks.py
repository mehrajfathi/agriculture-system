from datetime import datetime, timedelta
from .notifications import NotificationSystem
from crops.models import FarmPlot
from weather.services import WeatherService

def check_irrigation_needs():
    plots = FarmPlot.objects.all()
    weather_service = WeatherService()
    
    for plot in plots:
        # Check if irrigation is needed based on last irrigation date and soil moisture
        if (datetime.now() - plot.last_irrigation) > timedelta(days=3) or plot.soil_moisture < 30:
            NotificationSystem.send_irrigation_reminder(plot.farmer, plot)

def check_weather_conditions():
    weather_service = WeatherService()
    plots = FarmPlot.objects.values('farmer').distinct()
    
    for plot in plots:
        weather_data = weather_service.get_weather_data(plot.latitude, plot.longitude)
        if weather_data['needs_alert']:
            NotificationSystem.send_weather_alert(plot.farmer, weather_data) 