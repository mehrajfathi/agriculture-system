from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import Farmer

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    user_type = forms.ChoiceField(
        choices=[('farmer', 'Farmer'), ('buyer', 'Buyer')],
        widget=forms.RadioSelect,
        initial='buyer',
        required=True
    )
    phone_number = forms.CharField(max_length=15, required=False)
    address = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}), required=False)
    farm_size = forms.DecimalField(max_digits=10, decimal_places=2, required=False)
    farm_location = forms.CharField(max_length=200, required=False)

    class Meta:
        model = Farmer
        fields = ['username', 'email', 'password1', 'password2', 'user_type', 
                 'phone_number', 'address', 'farm_size', 'farm_location']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Farmer.objects.filter(email=email).exists():
            raise ValidationError('This email address is already in use.')
        return email

    def clean(self):
        cleaned_data = super().clean()
        user_type = cleaned_data.get('user_type')
        farm_size = cleaned_data.get('farm_size')
        farm_location = cleaned_data.get('farm_location')

        if user_type == 'farmer':
            if not farm_size:
                self.add_error('farm_size', 'Farm size is required for farmers')
            if not farm_location:
                self.add_error('farm_location', 'Farm location is required for farmers')

        return cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add Bootstrap classes to form fields
        for field in self.fields.values():
            if isinstance(field.widget, forms.TextInput) or \
               isinstance(field.widget, forms.EmailInput) or \
               isinstance(field.widget, forms.PasswordInput) or \
               isinstance(field.widget, forms.Textarea):
                field.widget.attrs.update({'class': 'form-control'}) 