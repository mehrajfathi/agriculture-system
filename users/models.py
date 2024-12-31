from django.contrib.auth.models import AbstractUser
from django.db import models

class Farmer(AbstractUser):
    USER_TYPE_CHOICES = [
        ('farmer', 'Farmer'),
        ('buyer', 'Buyer'),
        ('admin', 'Admin'),
    ]
    
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='buyer')
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    farm_size = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    farm_location = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users' 