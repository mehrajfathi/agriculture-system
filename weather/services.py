import requests
from django.conf import settings

class WeatherService:
    def __init__(self):
        self.api_key = "YOUR_API_KEY"  # Get from OpenWeatherMap
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"

    def get_weather_data(self, lat=12.9716, lon=77.5946):  # Default coordinates
        try:
            params = {
                'lat': lat,
                'lon': lon,
                'appid': self.api_key,
                'units': 'metric'
            }
            response = requests.get(self.base_url, params=params)
            data = response.json()

            if response.status_code == 200:
                return {
                    'temp': round(data['main']['temp']),
                    'humidity': data['main']['humidity'],
                    'wind_speed': round(data['wind']['speed'] * 3.6),  # Convert to km/h
                    'conditions': data['weather'][0]['main']
                }
            else:
                return self.get_mock_data()
                
        except Exception as e:
            print(f"Weather API error: {e}")
            return self.get_mock_data()

    def get_mock_data(self):
        return {
            'temp': 25,
            'humidity': 65,
            'wind_speed': 12,
            'conditions': 'Partly Cloudy'
        }

    def get_forecast(self):
        # Mock forecast data
        return [
            {'day': 'Today', 'temp': 25, 'conditions': 'Sunny'},
            {'day': 'Tomorrow', 'temp': 23, 'conditions': 'Cloudy'},
            {'day': 'Day 3', 'temp': 24, 'conditions': 'Partly Cloudy'}
        ]

    def get_alerts(self):
        # Mock alerts
        return [
            {'type': 'Rain Alert', 'message': 'Heavy rain expected tomorrow'},
            {'type': 'Temperature Alert', 'message': 'High temperature expected'}
        ] 