from django.contrib import admin
from .models import SinCalculation

@admin.register(SinCalculation)
class SinCalculationAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'angle', 'result')