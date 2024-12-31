from django.urls import path
from . import views

app_name = 'farm_management'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('plots/add/', views.farm_plot_create, name='farm_plot_create'),
    path('plots/<int:pk>/', views.farm_plot_detail, name='farm_plot_detail'),
    path('plots/<int:pk>/edit/', views.farm_plot_update, name='farm_plot_update'),
    path('plots/<int:pk>/delete/', views.farm_plot_delete, name='farm_plot_delete'),
] 