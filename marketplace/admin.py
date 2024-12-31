from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'seller', 'crop_type', 'price', 'quantity', 'unit', 'created_at']
    list_filter = ['crop_type', 'created_at']
    search_fields = ['title', 'description', 'seller__username']
    date_hierarchy = 'created_at'
    readonly_fields = ['created_at', 'updated_at']
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if not request.user.is_superuser:
            return qs.filter(seller=request.user)
        return qs
