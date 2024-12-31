from django.core.mail import send_mail
from django.conf import settings

class NotificationSystem:
    @staticmethod
    def send_email_notification(user, subject, message):
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [user.email],
            fail_silently=False,
        )

    @staticmethod
    def send_weather_alert(user, weather_data):
        subject = "Weather Alert for Your Farm"
        message = f"""
        Important Weather Update:
        Temperature: {weather_data['temp']}°C
        Conditions: {weather_data['conditions']}
        Recommended Actions: {weather_data['recommendations']}
        """
        NotificationSystem.send_email_notification(user, subject, message)

    @staticmethod
    def send_irrigation_reminder(user, plot):
        subject = "Irrigation Reminder"
        message = f"""
        Your {plot.crop.name} plot might need irrigation.
        Last irrigation: {plot.last_irrigation}
        Current soil moisture: {plot.soil_moisture}%
        """
        NotificationSystem.send_email_notification(user, subject, message) 