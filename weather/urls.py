from django.urls import path
from . import views

app_name = 'weather'

urlpatterns = [
    path('', views.weather_dashboard, name='dashboard'),
    path('forecast/', views.forecast, name='forecast'),
    path('alerts/', views.alerts, name='alerts'),
] 