from django.db import models

class YourNewModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'your_new_app'  # Important!

    def __str__(self):
        return self.name 