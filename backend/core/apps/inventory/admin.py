from django.contrib import admin
from .models import RoastBatch

@admin.register(RoastBatch)
class RoastBatchAdmin(admin.ModelAdmin):
    list_display = [
        "batch_number",
        "coffee",
        "roast_date", 
        "roasted_yield_kg",
        "status"
    ]

    list_filter = [
        "status",
        "roast_date"
    ]

    search_fields = [
        "batch_number", 
        "coffee__name"
    ]