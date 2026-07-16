from django.contrib import admin
from .models import Designation


@admin.register(Designation)
class DesignationAdmin(admin.ModelAdmin):
    list_display = ("code", "name", "is_active")
    search_fields = ("code", "name")
    list_filter = ("is_active",)
