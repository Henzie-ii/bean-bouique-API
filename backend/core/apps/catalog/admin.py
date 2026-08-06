from django.contrib import admin
from .models import Coffee, ProductVariant

class ProductVariantInline(admin.TabularInline):
    model = ProductVariant
    extra = 1

@admin.register(Coffee)
class CoffeeAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "origin",
        "process_method",
        "roast_level",
        "is_active"
    ]

    list_filter = [
        "process_method", 
        "roast_level",
        "is_active"
    ]

    search_fields = [
        "name", 
        "origin",
        "tasting_notes"
    ]

    prepopulated_fields = { "slug": ["name"]}

    inlines = [ProductVariantInline]

@admin.register(ProductVariant)
class ProductVariantAdmin(admin.ModelAdmin):
    list_display = [
        "stock_keeping_unit",
        "weight_grams",
        "grind_option",
        "price_cents"
    ]

    list_filter = [
        "grind_option",
        "weight_grams",
        "is_available"
    ]

    search_fields = [
        "stock_keeping_unit",
        "coffee__name,"
    ]

    
