from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Crop, FarmPlot
from .forms import FarmPlotForm

@login_required
def dashboard(request):
    user_plots = FarmPlot.objects.filter(farmer=request.user)
    context = {
        'plots': user_plots,
        'weather_data': get_weather_data(),  # Implementation needed
    }
    return render(request, 'crops/dashboard.html', context)

@login_required
def add_farm_plot(request):
    if request.method == 'POST':
        form = FarmPlotForm(request.POST)
        if form.is_valid():
            plot = form.save(commit=False)
            plot.farmer = request.user
            plot.save()
            return redirect('dashboard')
    else:
        form = FarmPlotForm()
    return render(request, 'crops/add_plot.html', {'form': form}) 