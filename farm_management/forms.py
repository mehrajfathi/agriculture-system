from django import forms
from .models import FarmPlot, Activity

class FarmPlotForm(forms.ModelForm):
    class Meta:
        model = FarmPlot
        fields = ['name', 'size', 'location', 'soil_type', 'crop_type', 'planting_date', 'expected_harvest_date']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter plot name'
            }),
            'size': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter size in acres',
                'min': '0',
                'step': '0.01'
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter location'
            }),
            'soil_type': forms.Select(attrs={
                'class': 'form-control'
            }),
            'crop_type': forms.Select(attrs={
                'class': 'form-control'
            }),
            'planting_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'expected_harvest_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            })
        }

    def clean(self):
        cleaned_data = super().clean()
        planting_date = cleaned_data.get('planting_date')
        harvest_date = cleaned_data.get('expected_harvest_date')
        
        if planting_date and harvest_date and harvest_date < planting_date:
            raise forms.ValidationError("Harvest date cannot be earlier than planting date")
        
        return cleaned_data

class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['activity_type', 'date', 'description', 'cost']
        widgets = {
            'activity_type': forms.Select(attrs={
                'class': 'form-control'
            }),
            'date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Enter activity description'
            }),
            'cost': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '0',
                'step': '0.01',
                'placeholder': 'Enter cost'
            })
        } 