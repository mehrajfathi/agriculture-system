from django.contrib import admin
from .models import FarmPlot, Activity

@admin.register(FarmPlot)
class FarmPlotAdmin(admin.ModelAdmin):
    list_display = ['name', 'farmer', 'size', 'location', 'soil_type', 'crop_type', 'created_at']
    list_filter = ['soil_type', 'crop_type', 'created_at']
    search_fields = ['name', 'location', 'farmer__username']
    date_hierarchy = 'created_at'

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ['activity_type', 'farm_plot', 'date', 'cost']
    list_filter = ['activity_type', 'date']
    search_fields = ['description', 'farm_plot__name']
    date_hierarchy = 'date'