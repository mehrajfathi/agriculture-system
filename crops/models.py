from django.db import models

class Crop(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    soil_type = models.CharField(max_length=100)
    climate_requirements = models.TextField()
    growing_season = models.CharField(max_length=100)
    water_requirements = models.TextField()
    fertilizer_requirements = models.TextField()

class FarmPlot(models.Model):
    farmer = models.ForeignKey('users.Farmer', on_delete=models.CASCADE)
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    soil_moisture = models.FloatField()
    soil_type = models.CharField(max_length=100)
    planting_date = models.DateField()
    last_irrigation = models.DateTimeField()
    last_fertilizer = models.DateTimeField() 