from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .services import WeatherService

@login_required
def weather_dashboard(request):
    weather_service = WeatherService()
    weather_data = weather_service.get_weather_data()
    context = {
        'weather_data': weather_data
    }
    return render(request, 'weather/dashboard.html', context)

@login_required
def forecast(request):
    weather_service = WeatherService()
    forecast_data = weather_service.get_forecast()
    context = {
        'forecast_data': forecast_data
    }
    return render(request, 'weather/forecast.html', context)

@login_required
def alerts(request):
    weather_service = WeatherService()
    alerts = weather_service.get_alerts()
    context = {
        'alerts': alerts
    }
    return render(request, 'weather/alerts.html', context) 