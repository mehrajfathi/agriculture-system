from django.db import models
from django.conf import settings
from django.db.models import Sum

class FarmPlot(models.Model):
    SOIL_TYPE_CHOICES = [
        ('clay', 'Clay Soil'),
        ('sandy', 'Sandy Soil'),
        ('loamy', 'Loamy Soil'),
        ('silty', 'Silty Soil'),
        ('peaty', 'Peaty Soil'),
        ('chalky', 'Chalky Soil'),
        ('black', 'Black Soil'),
    ]

    CROP_CHOICES = [
        ('rice', 'Rice'),
        ('wheat', 'Wheat'),
        ('corn', 'Corn'),
        ('sugarcane', 'Sugarcane'),
        ('cotton', 'Cotton'),
        ('vegetables', 'Vegetables'),
        ('fruits', 'Fruits'),
        ('pulses', 'Pulses'),
        ('other', 'Other'),
    ]

    farmer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    size = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=200)
    soil_type = models.CharField(max_length=50, choices=SOIL_TYPE_CHOICES, default='loamy')
    crop_type = models.CharField(max_length=50, choices=CROP_CHOICES, default='other')
    planting_date = models.DateField(null=True, blank=True)
    expected_harvest_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.farmer.username}"

    @classmethod
    def get_total_area(cls, user):
        return cls.objects.filter(farmer=user).aggregate(
            total_area=Sum('size'))['total_area'] or 0

class Crop(models.Model):
    CROP_STATUS_CHOICES = [
        ('planning', 'Planning'),
        ('planted', 'Planted'),
        ('growing', 'Growing'),
        ('harvested', 'Harvested'),
        ('failed', 'Failed'),
    ]

    farm_plot = models.ForeignKey(FarmPlot, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    variety = models.CharField(max_length=200)
    planting_date = models.DateField()
    expected_harvest_date = models.DateField()
    status = models.CharField(max_length=20, choices=CROP_STATUS_CHOICES, default='planning')
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} at {self.farm_plot.name}"

class Activity(models.Model):
    ACTIVITY_TYPE_CHOICES = [
        ('irrigation', 'Irrigation'),
        ('fertilization', 'Fertilization'),
        ('pesticide', 'Pesticide Application'),
        ('weeding', 'Weeding'),
        ('harvesting', 'Harvesting'),
        ('other', 'Other'),
    ]

    farm_plot = models.ForeignKey(
        FarmPlot, 
        on_delete=models.CASCADE, 
        related_name='activities',
        null=True,
        blank=True
    )
    activity_type = models.CharField(max_length=20, choices=ACTIVITY_TYPE_CHOICES, default='other')
    date = models.DateField()
    description = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Activities'

    def __str__(self):
        return f"{self.activity_type} for {self.farm_plot.name if self.farm_plot else 'Unknown Plot'}"

class MoistureReading(models.Model):
    farm_plot = models.ForeignKey(FarmPlot, on_delete=models.CASCADE)
    reading_value = models.DecimalField(max_digits=5, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Moisture reading for {self.farm_plot.name}: {self.reading_value}%"

    class Meta:
        ordering = ['-timestamp']
