from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import FarmPlot, Activity
from .forms import FarmPlotForm, ActivityForm

@login_required
def dashboard(request):
    farm_plots = FarmPlot.objects.filter(farmer=request.user).order_by('-created_at')
    total_area = FarmPlot.get_total_area(request.user)
    
    return render(request, 'farm_management/dashboard.html', {
        'farm_plots': farm_plots,
        'total_area': total_area,
        'title': 'Dashboard'
    })

@login_required
def farm_plot_create(request):
    if request.method == 'POST':
        form = FarmPlotForm(request.POST)
        if form.is_valid():
            farm_plot = form.save(commit=False)
            farm_plot.farmer = request.user
            farm_plot.save()
            messages.success(request, 'Farm plot created successfully!')
            return redirect('farm_management:dashboard')
    else:
        form = FarmPlotForm()
    
    return render(request, 'farm_management/farm_plot_form.html', {
        'form': form,
        'title': 'Add Farm Plot'
    })

@login_required
def farm_plot_update(request, pk):
    farm_plot = get_object_or_404(FarmPlot, pk=pk, farmer=request.user)
    
    if request.method == 'POST':
        form = FarmPlotForm(request.POST, instance=farm_plot)
        if form.is_valid():
            form.save()
            messages.success(request, 'Farm plot updated successfully!')
            return redirect('farm_management:dashboard')
    else:
        form = FarmPlotForm(instance=farm_plot)
    
    return render(request, 'farm_management/farm_plot_form.html', {
        'form': form,
        'farm_plot': farm_plot,
        'title': 'Edit Farm Plot'
    })

@login_required
def farm_plot_delete(request, pk):
    farm_plot = get_object_or_404(FarmPlot, pk=pk, farmer=request.user)
    if request.method == 'POST':
        farm_plot.delete()
        messages.success(request, 'Farm plot deleted successfully!')
        return redirect('farm_management:dashboard')
    
    return render(request, 'farm_management/farm_plot_confirm_delete.html', {
        'farm_plot': farm_plot,
        'title': 'Delete Farm Plot'
    })

@login_required
def farm_plot_detail(request, pk):
    farm_plot = get_object_or_404(FarmPlot, pk=pk, farmer=request.user)
    activities = farm_plot.activities.all().order_by('-date')
    
    return render(request, 'farm_management/farm_plot_detail.html', {
        'farm_plot': farm_plot,
        'activities': activities,
        'title': farm_plot.name
    })
