from django.contrib import admin
from .models import VorstandMitglied

@admin.register(VorstandMitglied)
class VorstandAdmin(admin.ModelAdmin):
    list_display = ('name', 'rolle', 'geschlecht')
    list_filter = ('rolle', 'geschlecht')
    search_fields = ('name', 'aufgabe')
