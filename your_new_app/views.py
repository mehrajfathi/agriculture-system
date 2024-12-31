from django.shortcuts import render
from .models import YourNewModel

def your_view(request):
    # This will automatically use the second database
    items = YourNewModel.objects.using('second_db').all()
    return render(request, 'your_template.html', {'items': items}) 