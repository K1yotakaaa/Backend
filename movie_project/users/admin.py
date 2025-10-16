from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    # What fields to display in the list view
    list_display = ('username', 'email', 'is_staff', 'is_superuser', 'is_admin')

    # What fields to filter by
    list_filter = ('is_staff', 'is_superuser', 'is_admin')

    # Add your custom field to the fieldsets (edit page)
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Permissions', {'fields': ('is_admin',)}),
    )

    # Add your custom field to the add user form
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Custom Permissions', {'fields': ('is_admin',)}),
    )
