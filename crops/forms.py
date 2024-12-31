from django import forms
from .models import FarmPlot, Crop

class FarmPlotForm(forms.ModelForm):
    class Meta:
        model = FarmPlot
        fields = ['crop', 'soil_moisture', 'soil_type', 'planting_date']
        widgets = {
            'planting_date': forms.DateInput(attrs={'type': 'date'}),
        }

class CropKnowledgeForm(forms.ModelForm):
    class Meta:
        model = Crop
        fields = '__all__' 