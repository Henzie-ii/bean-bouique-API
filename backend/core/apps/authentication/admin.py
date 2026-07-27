from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomerUserAdmin(UserAdmin):
    model = User

    #table views in admin

    list_display = [
        "username",
        "email",
        "default_grind_preference",
        "is_staff",
        "is_active"
    ]
    list_filter = [
        "role",
        "is_staff", 
        "is_active"
    ]

    # Detail edit screen
    fieldsets = UserAdmin.fieldsets + (
        ("Bean Boutique Profile", {
            "fields":("role", "default_grid_preference", "phone_number")
        },),
    )

    #User creation screen
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Bean Boutique Profile", {
            "fields":("role", "default_grind_preferences", "phone_number")
        },),
    )

